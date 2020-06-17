from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import Pipeline
from azureml.core import Workspace
from azureml.pipeline.core.graph import PipelineParameter
from azureml.core import Experiment

from azureml.core.runconfig import RunConfiguration
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.runconfig import DEFAULT_CPU_IMAGE
from uuid import uuid4

from modelManager import ModelManager
import os

ws = Workspace.from_config(path='.cloud/.azureml/', _file_name='config.json')


run_config = RunConfiguration.load('.cloud/.azureml/aml_run_config.yml')

arguments = ModelManager.GetPipelineArguments('./MLproject', 'training')

trainStep = PythonScriptStep(
    script_name="src/luna/train.py",
    arguments=arguments,
    inputs=[],
    outputs=[],
    source_directory=os.getcwd(),
    runconfig=run_config
)

pipeline1 = Pipeline(workspace=ws, steps=[trainStep])

experiment = Experiment(ws, 'mlFlowtest')
experiment.set_tags(tags={'userId': 'xiwu@microsoft.com', 'productName': 'eddi', 'deploymentName': 'westus', 'apiVersion':'v1.0'})
pipeline_run1 = experiment.submit(pipeline1)