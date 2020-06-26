from luna import utils
from LunaPythonModel import LunaPythonModel

def init():
    global python_model
    python_model = LunaPythonModel()

def run(userInput):
    return python_model.predict(None, userInput)