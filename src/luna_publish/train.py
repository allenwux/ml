from luna import utils
import os
import mlflow
from mlflow.pyfunc import PythonModel, PythonModelContext

class LunaPythonModel(PythonModel):
    def load_context(self, context):
        return

    def predict(self, context, model_input):
        return model_input

#mlflow.set_tracking_uri('databricks')

#mlflow.start_run(experiment_id=73511552574955)

#args, userInput = utils.ParseArguments("training")

# train your model here
# userInput is a dictionary, for example userInput['source']

# update the model_path to locate your model
# update the description
#utils.RegisterModel(model_path = 'models',
#                       description = "your model description",
#                       args=args)

mlflow.start_run()
model_path = 'models'
mlFlowRun = mlflow.active_run()
print(mlFlowRun)
if mlFlowRun:
    mlflow.pyfunc.log_model(artifact_path=model_path, 
        python_model=LunaPythonModel(), 
        artifacts={'MLFLOW_MODEL': 'models'}, 
        conda_env=mlflow.pyfunc.get_default_conda_env())
    model_uri = "runs:/{run_id}/{artifact_path}".format(run_id=mlFlowRun.info.run_id, artifact_path=model_path)
    print(model_uri)
    result = mlflow.register_model(
        model_uri,
        #args.modelId
        'defaultModelId'
    )
    print(result)

mlflow.end_run()