from flask import Flask, render_template
from flask_socketio import SocketIO
from TankController import *
import json
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins='*')
#BootStrap

# Start Tank
motor_init()

@socketio.on('command')
def handle_my_custom_event(payload):
    
    command = payload["actionType"]
    print(command)
    if command == "moveUp":
        run(1)
    elif command == "moveDown" :
        back(1)
    elif command == "moveRight" :
        right(1)
    elif command == "moveLeft" :
        left(1)
        pass
    elif command == "topTankMovement" :
        brake(1)
        pass
    elif command == "spinTankRight" :
        spin_right(1)
        pass
    elif command == "spinTankLeft" :
        spin_left(1)
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass

@socketio.on('connect')
def handle_connection():
    print('received json: ')

if __name__ == '__main__':
    socketio.run(app)