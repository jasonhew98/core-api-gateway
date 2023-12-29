# config.py
import json

class Configuration:
    def __init__(self, environment='production'):
        # Load default settings from appsettings.json
        with open('appsettings.json') as config_file:
            config_data = json.load(config_file)
            self.__dict__.update(config_data)

        # Load environment-specific settings from appsettings.<environment>.json
        environment_config_file = f'appsettings.{environment}.json'
        try:
            with open(environment_config_file) as env_config_file:
                env_config_data = json.load(env_config_file)
                self.__dict__.update(env_config_data)
        except FileNotFoundError:
            pass  # Ignore if the environment-specific file is not found
