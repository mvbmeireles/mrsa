from mrsa import roboMRSA
from flask import Flask

app = Flask(__name__)

@app.route('/<string:command>')
def commands(command):
    robot = roboMRSA()
    command = command.upper()
    if not checkComands(command):
        return ("400 Bad Request", 400)

    return robot.mrsa(command)

def checkComands(robotMoveList):
    acceptsCommandsToRobot = ["M", "L", "R"]
    for move in robotMoveList:
        if move not in acceptsCommandsToRobot:
            return False
    return True

app.run(debug=True)