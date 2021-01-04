from utils.util import get_path_of_workflow_file
from utils.py2ipynb import py2ipynb

def execute_script(c_name):
    python_script = get_path_of_workflow_file(__file__, 'output.py')
    py2ipynb(python_script, '%s.ipynb' % (c_name), "spyder",  ["# ----------------------------------------------------------------------------"])

