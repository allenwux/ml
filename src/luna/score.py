from modelManager import ModelManager

def init():
    global model_path
    model_path = ModelManager.GetModelPath()

def run(userInput):
    print(userInput)