import json

with open("../config/boss_config.json") as config_file_handler:
    conf = json.load(config_file_handler)



class BossConfig:
    def __init__(self):
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]
