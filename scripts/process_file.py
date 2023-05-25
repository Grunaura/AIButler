'''
Author: Adam Messick
Date: 5/24/2023
This file contains the code to read content from a file.
'''

def read_file_content(filepath):
    '''
    Reads the content of a given file.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The content of the file.
    '''
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None
