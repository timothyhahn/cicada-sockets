# -*- coding: utf-8 -*-

from tornado import websocket

# TODO: This will not scale, obviously - let's figure it out in a bit.
handlers = []


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):  # pragma: no cover
        return True

    def open(self):
        if self not in handlers:
            handlers.append(self)
        self.write_message('Connected!')

    def on_close(self):
        if self in handlers:
            handlers.remove(self)

    def on_message(self, message):
        other_handlers = filter(lambda handler: handler is not self, handlers)
        for handler in other_handlers:
            handler.write_message(message)
