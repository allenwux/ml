from modelManager import ModelManager
import os

args, userInput = ModelManager.ParseArguments("deployment")

# train your model here
# userInput is a dictionary, for example userInput['source']

# update the model_path to locate your model
# update the description
ModelManager.RegisterModel(model_path = 'models',
                       description = "your model description",
                       args=args)