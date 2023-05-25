'''
Author: Adam Messick
Date: 5/24/2023
This file contains the code to process a written language query or command.
'''

class CommandProcessor:
    '''
    Class to hold and manage the processing of commands.
    '''
    def __init__(self, options):
        '''
        Initializes the command processor with default values.

        Args:
            options (Options): An instance of the Options class.
        '''
        self.options = options

    def process_command(self, command):
        '''
        Processes the input command and executes the corresponding method.

        Args:
            command (str): The input command.
        '''
        method_name = 'command_' + command
        method = getattr(self, method_name, self.invalid_command)
        return method()

    def command_help(self):
        '''
        Provides help information.
        '''
        return 'Help information'

    def command_exit(self):
        '''
        Exits the application.
        '''
        exit()

    def invalid_command(self):
        '''
        Handles invalid commands.
        '''
        return 'Invalid command'
