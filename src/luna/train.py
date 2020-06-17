from modelManager import ModelManager
import os

args, userInput = ModelManager.ParseArguments("deployment")

## train your model here

os.mkdir('./mymodel')

f = open("./mymodel/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
print('registering model')

ModelManager.RegisterModel(model_path = './mymodel',
                       description = "EDDI for boston",
                       args=args)