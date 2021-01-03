import json
import os

class Configuration(object):
    def __init__(self, config_filename, configuration_level=None):
        self._configuration_level = configuration_level
        self.__get_config(config_filename)
       
        if self._configuration_level is not None and self._configuration_level not in self._config.keys():
            raise AttributeError("'{}' key not found in 'config.json'".format(configuration_level))

    def __get_config(self, config_filename):
        holding_directory = os.path.dirname(__file__)
        self.local_configuration_file = os.path.join(holding_directory, config_filename +'.config.json')
        
        with open(self.local_configuration_file) as config_file:
                self._config = json.load(config_file)


    def get_property(self, property_name):
        config = self._config
        if self._configuration_level is not None:
            config = self._config[self._configuration_level]

        if property_name not in config.keys():
            return None

        return config[property_name]