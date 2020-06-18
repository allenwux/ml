from luna import utils
import os

args, userInput = utils.ParseArguments("inference")

# define your own temp model path
model_path = os.path.join(os.getcwd(), "models", args.modelId)
utils.DownloadModel(args.modelId, model_path)

# Do your batch inference here. You model is the following directory: model_path/<model_path you specified in train.py>
# userInput is a dictionary, for example userInput['source']