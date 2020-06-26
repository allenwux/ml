from mlflow.pyfunc import PythonModel, PythonModelContext
from luna import utils

class LunaPythonModel(PythonModel):
    def load_context(self, context):
        global model_path   
        model_path = utils.GetModelPath()

    def predict(self, context, model_input):
        # Add your scoring code here. You model is the following directory: model_path/<model_path you specified in train.py>
        # DO NOT use context otherwise it won't work on Azure ML
        return model_input