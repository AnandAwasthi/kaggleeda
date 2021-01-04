from termcolor import colored, cprint
from config_file import Configuration


config = Configuration('competition')
c_name = config.get_property('ref')

def _intro():
    text = """\
        %s EDA
        %s
            Organization Name: %s
            Evaluation Metric: %s
            Is Kernels Submissions Only: %s
            """ % (
                    config.get_property('title'), 
                    config.get_property('description'),
                    config.get_property('organizationName'),
                    config.get_property('evaluationMetric'),
                    config.get_property('isKernelsSubmissionsOnly')
                    )

    print(colored(text, 'green', attrs=['bold']))

def _content_index():
    text = """\
        Content
            Prepare the data analysis
                Data exploration
                    Check the data
                    Density plots of features
                    Distribution of mean & max
                    Distribution of skew & kurtosis
                    Feature correlations
                    Duplicate values
                Feature engineering
            """

    print(colored(text, 'blue', attrs=['bold']))

def dummpy():
    return 1 + 3
def get_result():
    
    _intro()
    _content_index()
    dummpy()
            
