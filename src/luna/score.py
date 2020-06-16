import util.ModelManager as modelManager

def init():
    global model_path
    model_path = modelManager.GetModelPath()

def run(userInput):
    print(userInput)