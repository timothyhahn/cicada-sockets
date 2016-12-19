# -*- coding: utf-8 -*-

# Third-party imports
from tornado import web, ioloop

# Project imports
import settings

# Submodule imports
from handlers import socket_handlers

app = web.Application([
	(r'/ws', socket_handlers.SocketHandler)
])

if __name__ == '__main__':
	app.listen(port=settings.PORT)
	print('Listening on {}'.format(settings.PORT))
	ioloop.IOLoop.instance().start()