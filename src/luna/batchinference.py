import utils.ModelManager as modelManager
import os

args, userInput = modelManager.ParseArguments("deployment")

# define your own temp model path
tmp_model_path = os.path.join(os.getcwd(), "tmp", args.modelId)
modelManager.DownloadModel(args.modelId, tmp_model_path)

# Do your batch inference here
