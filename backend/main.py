from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins='*')

@socketio.on('command')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('connect')
def handle_connection(json):
    print('received json: ' + str(json))
if __name__ == '__main__':
    socketio.run(app)