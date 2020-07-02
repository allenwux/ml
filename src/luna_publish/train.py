from luna.lunaUtils import LunaUtils
import os
from LunaPythonModel import LunaPythonModel

utils = LunaUtils.Create(run_type = 'training')
args = utils.args
userInput = utils.userInput

python_model = LunaPythonModel()

model_path, description = python_model.train(args, userInput)


utils.RegisterModel(model_path = model_path,
                       description = description,
                       luna_python_model=LunaPythonModel())