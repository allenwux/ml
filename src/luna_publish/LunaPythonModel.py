from mlflow.pyfunc import PythonModel, PythonModelContext
from luna.lunaUtils import LunaUtils

class LunaPythonModel(PythonModel):
    def load_context(self, context):
        ## DO NOT CHANGE! Set mlflow as default run mode
        self._run_mode = 'mlflow'

        # This function will only be called if user deploy the model to a real time service endpoint
        # This function will be called every time when the container instance is started
        # DO NOT use context otherwise it won't work on Azure ML
        return

    def predict(self, context, model_input):
        ## DO NOT CHANGE! Get the model path
        model_path = LunaUtils.GetModelPath(run_mode = self._run_mode, context = context)

        # Add your scoring code here. You model is the following directory: model_path/<model_path you specified in train method>
        # DO NOT use context otherwise it won't work on Azure ML
        # Update the scoring_result with the real result

        scoring_result = 'result'
        return scoring_result

    def train(self, args, user_input):
        # train your model here
        # userInput is a dictionary, for example userInput['source']

        # Update the model_path if your model is saved in a different folder. 
        # All files under model_path will be saved and registered as a part of the model
        # Update the description for your model
        model_path = 'models'
        description = 'this is my model description'
        return model_path, description

    def batch_inference(self, args, user_input, model_path):
        # Do your batch inference here. You model is the following directory: model_path/<model_path you specified in train method>
        # userInput is a dictionary, for example userInput['source'] or userInput['hyper_parameters]['epocs']
        # The return value will be ignored. You should ask user to provide a output data source as user input and write the result
        return

    ## DO NOT CHANGE
    def set_run_mode(self, run_mode):
        self._run_mode = run_mode
