from luna import utils
import os

def init():
    global model_path   
    model_path = utils.GetModelPath()

def run(userInput):
    # Add your scoring code here. You model is the following directory: model_path/<model_path you specified in train.py>
    return userInput