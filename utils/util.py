import os

def get_path_of_workflow_file(caller_script_file, referenced_file):

    holding_directory = os.path.dirname(os.path.realpath(caller_script_file))
    return os.path.join(holding_directory, referenced_file)