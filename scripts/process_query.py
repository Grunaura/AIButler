'''
Author: Adam Messick
Date: 5/24/2023
This file contains the code to process a written language query or command.
'''

import openai

class QueryProcessor:
    '''
    Class to hold and manage the processing of written language queries or commands.
    '''
    def __init__(self, options):
        '''
        Initializes the query processor with default values.

        Args:
            options (Options): An instance of the Options class.
        '''
        self.options = options
        self.openai_api_key = "Your OpenAI API Key"

    def process_query(self, query):
        '''
        Processes the input query using the OpenAI GPT model.

        Args:
            query (str): The input query.

        Returns:
            dict: The output from the GPT model.
        '''
        openai.api_key = self.openai_api_key
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=query,
          max_tokens=150,
          temperature=self.options.get_options()['temperature'],
        )

        return response.choices[0].text.strip()

