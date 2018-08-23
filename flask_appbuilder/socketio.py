from flask_socketio import SocketIO

from .basemanager import BaseManager


class SocketIOManager(BaseManager):
    def __init__(self, appbuilder):
        super(SocketIOManager, self).__init__(appbuilder)
        app = appbuilder.get_app
        self.socketio = SocketIO(app)

    def run(self, *args, **kwargs):
        return self.socketio.run(*args, **kwargs)

    def on(self, *args, **kwargs):
        return self.socketio.on(*args, **kwargs)
