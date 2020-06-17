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

from src.luna.utils import pipelineManager
import os

ws = Workspace.from_config(path='.cloud/.azureml/', _file_name='default_workspace.json')

run_id = pipelineManager.RunProject(azureml_workspace = ws, 
                                    entry_point = 'deployment', 
                                    experiment_name = 'mlFlowtest', 
                                    parameters={'modelId': 'anewmodel', 'endpointId': 'anewendpoint'}, 
                                    tags={'userId': 'xiwu@microsoft.com', 'productName': 'eddi', 'deploymentName': 'westus', 'apiVersion':'v1.0'})

print(run_id)