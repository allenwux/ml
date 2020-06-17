from modelManager import ModelManager
from azureml.core.model import Model
from azureml.core import Run
from azureml.core import Workspace
from azureml.core.environment import Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AksWebservice, AciWebservice, Webservice
from modelManager import ModelManager
from azureml.core.runconfig import RunConfiguration

from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import Pipeline
from azureml.core import Workspace
from azureml.pipeline.core.graph import PipelineParameter
from azureml.core import Experiment

import os
import yaml


def Init(luna_config_file='luna_config.yml'):
    with open(luna_config_file) as file:
        luna_config = yaml.full_load(file)
    return luna_config

def GetDeploymentConfig(luna_config, dns_name_label):
    with open(luna_config['azureml']['workspace_config']) as file:
        documents = yaml.full_load(file)
        deployment_target = documents['deployment_target']
        aks_cluster = documents['aks_cluster']


    with open(luna_config['deploy_config']) as file:
        documents = yaml.full_load(file)

        if deployment_target == 'aci':
            deployment_config = AciWebservice.deploy_configuration()
            deployment_config.__dict__.update(documents['azureContainerInstance'])
            deployment_config.dns_name_label = dns_name_label
        elif deployment_target == 'aks':
            deployment_config = AksWebservice.deploy_configuration()
            deployment_config.__dict__.update(documents['kubernetes'])
            deployment_config.compute_target_name = aks_cluster
            deployment_config.namespace = dns_name_label

    return deployment_config

def DeployModel():

    luna_config = Init()

    args, userInput = ModelManager.ParseArguments("deployment")

    dns_name_label = userInput["dns_name_label"]
    model_id = args.modelId
    endpoint_id = args.endpointId

    print(dns_name_label)


    run = Run.get_context()

    ## If it is running in AML context
    if run:
        experiment = Run.get_context(allow_offline=False).experiment
        ws = experiment.workspace
        model = Model(ws, model_id)

        print(model)

        myenv = Environment.from_conda_specification('scoring', luna_config['conda_env'])

        print(luna_config['code']['score'])
        print(os.getcwd())

        inference_config = InferenceConfig(entry_script=luna_config['code']['score'], source_directory = os.getcwd(), environment=myenv)

        deployment_config = GetDeploymentConfig(luna_config, dns_name_label)
        
        service = Model.deploy(ws, endpoint_id, [model], inference_config, deployment_config)
        service.wait_for_deployment(show_output = True)

def RunProject(azureml_workspace, entry_point, experiment_name, parameters, tags):

    luna_config = Init()
    if azureml_workspace:
        run_config = RunConfiguration.load(luna_config['azureml']['run_config'])

        arguments = GetPipelineArguments(luna_config['MLproject'], entry_point, parameters)

        trainStep = PythonScriptStep(
            script_name=luna_config['code'][entry_point],
            arguments=arguments,
            inputs=[],
            outputs=[],
            source_directory=os.getcwd(),
            runconfig=run_config
        )

        pipeline = Pipeline(workspace=azureml_workspace, steps=[trainStep])

        experiment = Experiment(azureml_workspace, experiment_name)
        pipeline_run = experiment.submit(pipeline, tags=tags)
        return pipeline_run.id
    
    else:
        return '00000000-0000-0000-0000-000000000000'

def GetPipelineArguments(mlproject_file_path, run_type, parameters):
    with open(mlproject_file_path) as file:
        documents = yaml.full_load(file)
        arguments = []
        for param in documents['entry_points'][run_type]['parameters']:
            pipelineParam = PipelineParameter(name=param, default_value=documents['entry_points'][run_type]['parameters'][param]['default'])
            argumentName = '--' + param
            arguments.append(argumentName)
            # get input parameter values, set default value if not provided
            if param in parameters:
                arguments.append(parameters[param])
            else:
                arguments.append(pipelineParam)
        return arguments