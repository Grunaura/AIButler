'''
Author: Adam Messick
Date: 5/24/2023
This file contains the code to set options for processing.
'''

class Options:
    '''
    Class to hold and manage the processing options.
    '''
    def __init__(self, temperature=0.5):
        '''
        Initializes the processing options with default values.

        Args:
            temperature (float, optional): Temperature value for the processing. Defaults to 0.5.
        '''
        self.temperature = temperature

    def set_temperature(self, temperature):
        '''
        Sets the temperature for the processing.

        Args:
            temperature (float): Temperature value for the processing.
        '''
        if 0 <= temperature <= 1:
            self.temperature = temperature
        else:
            raise ValueError("Temperature must be between 0 and 1")

    def get_options(self):
        '''
        Returns the current options as a dictionary.

        Returns:
            dict: A dictionary of options.
        '''
        return {
            "temperature": self.temperature,
        }
