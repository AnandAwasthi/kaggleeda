import os, json
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleKernel:
    def __init__(self, user_id, user_key, c_name, holding_directory):
        self.holding_directory = holding_directory
        KAGGLE_CONFIG_DIR = os.path.join(os.path.expandvars(os.getenv('USERPROFILE')), '.kaggle')
        os.makedirs(KAGGLE_CONFIG_DIR, exist_ok = True)
        with open(os.path.join(KAGGLE_CONFIG_DIR, 'kaggle.json'), 'w') as f:
            json.dump({'username': user_id, 'key': user_key}, f)
        self.kaggleApi = KaggleApi()
        self.user_id = user_id
        self.c_name = c_name
        
    def authenticate(self):
        self.kaggleApi.authenticate()

    def create_metadatafile(self, pynbfilePath):
        with open(os.path.join(self.holding_directory, 'kernel-metadata.json'), 'w') as f:
            json.dump({
                "id": '%s/%s' % (self.user_id, self.c_name),
                "title": "automated kernel",
                "code_file": pynbfilePath,
                "language": "python",
                "kernel_type": "notebook",
                "is_private": "true",
                "enable_gpu": "false",
                "enable_internet": "true",
                "dataset_sources": [],
                "competition_sources": [self.c_name],
                "kernel_sources": []
                }, f)

    def competition(self):
        competitions = self.kaggleApi.competitions_list(search = self.c_name)
        for competition in competitions:
            if str(competition) == self.c_name:
                with open(os.path.join(self.holding_directory, 'competition.config.json'), 'w') as f:
                    json.dump({
                        "title": getattr(competition, 'title'),
                        "description":getattr(competition, 'description'),
                        "organizationName": getattr(competition, 'organizationName'),
                        "evaluationMetric": getattr(competition, 'evaluationMetric'),
                        "kernel_type": "notebook",
                        "is_private": "true",
                        "enable_gpu": "false",
                        "enable_internet": "true",
                        "dataset_sources": [],
                        "competition_sources": [self.c_name],
                        "kernel_sources": []
                        }, f)
                return competition

    def push(self):
        self.kaggleApi.kernels_push(self.holding_directory)