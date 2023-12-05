import argparse
# from optparse import OptionParser

class ParametersTest:
    def __init__(self, **kwargs):
        self.param1 = kwargs.get("param1")
        self.param2 = kwargs.get("param2")

def view_parameters(input_parameters):
    print(input_parameters.param1)
    print(input_parameters.param2)

parser = argparse.ArgumentParser(description='Passing parameters in an object')

parser.add_argument("-p1", dest="param1", help="parameter1")

parser.add_argument("-p2", dest="param2", help="parameter2")

params = parser.parse_args()

input_parameters = ParametersTest(param1=params.param1,param2=params.param2)

view_parameters(input_parameters)