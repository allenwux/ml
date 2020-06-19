## Update your code
- Update src/luna/train.py and add your training code
  - Add your training code
  - Save your model in *models* folder. You can save the model in a subdirectory, or a diffrent folder (not recommended)
  - If your model is saved in a subdirectory of *models* folder or a different directory, update the *model_path* argument in the RegisterModel call
  - Update the description argument in the RegisterModel call
- Update src/luna/batchinference.py and add your batch inference code
  -  Update the value of *model_path* variable if you want to download model to a different folder
  -  Add your inference code
  -  Delete the downloaded model after inference
- Update the run function in src/luna/score.py and add your scoring code
  - Add anything you need to run when the container instance startes and every time when it restarts to the *init()* function
  - Add your scoring code in the *run()* function and return the result. Use *model_path* global variable to locate your model (pre-downloaded to the container)

## Update your environment
- Update the conda.yml to add your conda or pip dependencies
- 

You are ready to go!