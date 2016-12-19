import uuid
from tornado import testing, httpserver, gen, web, websocket
from handlers import socket_handlers


class TestChatHandler(testing.AsyncTestCase):
    # TODO: Add testing for alternative origins. Might need Docker for this.

    def setUp(self):
        super(TestChatHandler, self).setUp()
        app = web.Application([(r'/', socket_handlers.SocketHandler)])
        server = httpserver.HTTPServer(app)
        socket, self.port = testing.bind_unused_port()
        server.add_socket(socket)

    def _get_connection(self):
        return websocket.websocket_connect(
            'ws://localhost:{}/'.format(self.port)
        )

    @gen.coroutine
    def _get_client(self):
        c = yield self._get_connection()

        # Discarding connection messages for clients
        yield c.read_message()

        raise gen.Return(c)

    @testing.gen_test
    def test_handshake(self):
        connection = yield self._get_connection()
        response = yield connection.read_message()
        self.assertEqual('Connected!', response)

    @testing.gen_test
    def test_multiple_clients(self):
        client1 = yield self._get_client()
        client1_id = str(uuid.uuid4())
        client2 = yield self._get_client()
        client2_id = str(uuid.uuid4())

        client1.write_message(client1_id)
        client2.write_message(client2_id)

        response1 = yield client1.read_message()
        response2 = yield client2.read_message()
        client1.close()
        client2.close()

        yield client1.read_message()
        yield client2.read_message()

        # Ensure they get each others messages - not their own.
        self.assertEquals(response1, client2_id)
        self.assertNotEquals(response1, client1_id)
        self.assertEquals(response2, client1_id)
        self.assertNotEquals(response2, client2_id)
