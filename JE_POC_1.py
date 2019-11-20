
from Step_1 import config, set_config



environment = 'Dev'

def Main(environment):
    parameter_dict = set_config(environment, config)

    print(parameter_dict)
