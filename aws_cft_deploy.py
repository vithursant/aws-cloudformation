import argparse
import os

class DeployEC2Instance:

    def __init__(self):
        self.args = None
        self.options = ['--stack-name',
                        '--template-body',
                        '--key-name',
                        '--instance-type']

    #@staticmethod
    def parseArgs(self, args):
        """
        Parse the arguments from the given command line
        Args:
            args (list<str>): List of arguments to parse. If None, the default sys.argv will be parsed
        """

        parser = argparse.ArgumentParser()

        instanceArgs = parser.add_argument_group('Instance options')

        instanceArgs.add_argument(self.options[0], type=str, default=None, help='add a name for the stack')
        instanceArgs.add_argument(self.options[1], type=str, default=None, help='add a template')
        instanceArgs.add_argument(self.options[2], type=str, default=None, help='add security key')
        instanceArgs.add_argument(self.options[3], type=str, default=None, help='add instance type')
        
        return parser.parse_args(args)

    def createStackCmd(self):
        command = 'aws cloudformation create-stack ' + \
                    self.options[0] + ' ' + self.args.stack_name + ' ' + \
                    self.options[1] + ' ' + 'file://' + self.args.template_body + ' ' + \
                    '--parameters ' + \
                    'ParameterKey=KeyName,ParameterValue=' + self.args.key_name + ' ' + \
                    'ParameterKey=InstanceType,ParameterValue=' + self.args.instance_type

        print (command)

    def main(self, args=None):
        self.args = self.parseArgs(args)
        self.createStackCmd()