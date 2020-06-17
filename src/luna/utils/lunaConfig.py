import yaml

class AzureMLConfig:
    run_config = ''
    workspace_config = ''
    
    def __init__(self, value_dict):
        self.__dict__.update(value_dict)

class MLFlowConfig:
    spark_config = ''
    workspace_config = ''
    
    def __init__(self, value_dict):
        self.__dict__.update(value_dict)

class LunaConfig:
    MLproject = ''
    supported_target = ''
    project_type = ''
    conda_env = ''
    deploy_config = ''

    def __init__(self, luna_config_file):
        global azureml, mlflow
        with open(luna_config_file) as file:
            documents = yaml.full_load(file)
            self.__dict__.update(documents)
            azureml = AzureMLConfig(documents['azureml'])
            mlflow = MLFlowConfig(documents['mlflow'])