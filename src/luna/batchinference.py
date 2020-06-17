from modelManager import ModelManager
import os

args, userInput = ModelManager.ParseArguments("deployment")

# define your own temp model path
tmp_model_path = os.path.join(os.getcwd(), "tmp", args.modelId)
ModelManager.DownloadModel(args.modelId, tmp_model_path)

# Do your batch inference here
