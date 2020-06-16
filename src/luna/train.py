import utils.ModelManager as modelManager

args, userInput = modelManager.ParseArguments("deployment")

## train your model here

modelManager.RegisterModel(model_path = './mymodel',
                       description = "EDDI for boston",
                       args=args)