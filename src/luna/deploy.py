from modelManager import ModelManager
from azureml.core.model import Model
from azureml.core import Run
from azureml.core import Workspace
from azureml.core.environment import Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AksWebservice, AciWebservice, Webservice

import os
from utils import pipelineManager

pipelineManager.DeployModel()