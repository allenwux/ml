from luna import utils
import os

args, userInput = utils.ParseArguments("deployment")

# train your model here
# userInput is a dictionary, for example userInput['source']

# update the model_path to locate your model
# update the description
utils.RegisterModel(model_path = 'models',
                       description = "your model description",
                       args=args)