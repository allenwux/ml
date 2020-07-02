from luna.lunaUtils import LunaUtils
import os

from LunaPythonModel import LunaPythonModel

utils = LunaUtils.Create(run_type = 'batchinference')
args = utils.args
userInput = utils.userInput

model_path = utils.DownloadModel()
print(model_path)

python_model = LunaPythonModel()

model_path = python_model.train(args, userInput)
