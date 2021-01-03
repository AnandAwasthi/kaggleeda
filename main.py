import os, json, pandas as pd
import nbformat as nbf
import sys
import subprocess
from runpy import run_path
from kaggle_kernel import KaggleKernel

def main():
    user_id, user_key, c_name, dataset_type = get_workflow_config()
    holding_directory = os.path.dirname(os.path.realpath(__file__))
    kaggleKernel = KaggleKernel(user_id, user_key, c_name, holding_directory)
    kaggleKernel.authenticate()
    
    workflow_config_file_path = os.path.join('.', dataset_type, 'config.py')
    config_script_results = run_path(workflow_config_file_path)
    config_script_results['execute_script'](c_name)
    pynbfilePath = os.path.join(holding_directory, '%s.ipynb' % (c_name))
    kaggleKernel.create_metadatafile(pynbfilePath)
    kaggleKernel.push()

def get_workflow_config():
    args = sys.argv
    if len(args) <= 3:
        print("Expected a userid, key & cname of the args")
        exit(0)
    user_id = args[1]
    user_key = args[2]
    c_name = args[3]
    dataset_type = args[4]
    return user_id, user_key, c_name, dataset_type



if __name__ == '__main__':
    main()


