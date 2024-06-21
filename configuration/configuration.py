import json

class AppConfig:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config_data = json.load(file)
        
        self.llm_base_url = config_data.get('llm_base_url')
        self.llm_api_key = config_data.get('llm_api_key')
        self.llm_model = config_data.get('llm_model')