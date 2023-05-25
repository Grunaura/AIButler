'''
-------------------------------------------------------------------------
Author: Adam Messick
Date: 5/24/2023
Description: This module contains various helper functions that can be
used throughout the application.
-------------------------------------------------------------------------
'''

import re
import logging
from datetime import datetime


def sanitize_input(input_string):
    '''
    A simple function to sanitize user input, removing any potentially malicious characters.
    '''
    sanitized = re.sub('[^A-Za-z0-9 ]+', '', input_string)
    return sanitized


def log_error(error_message):
    '''
    A function to log error messages in a standardized way.
    '''
    logging.error(f'{datetime.now()} - {error_message}')


def format_date(date):
    '''
    A function to format date objects for consistent display.
    '''
    return date.strftime('%Y-%m-%d %H:%M:%S')


def log_event(event_message):
    '''
    A function to log general events in a standardized way.
    '''
    logging.info(f'{datetime.now()} - {event_message}')


def network_request(url):
    '''
    A function to standardize network requests.
    '''
    response = requests.get(url)
    return response


def write_to_db(connection, query, data):
    '''
    A function to standardize database write operations.
    '''
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()


def read_from_db(connection, query):
    '''
    A function to standardize database read operations.
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def read_from_file(file_path):
    '''
    A function to standardize file read operations.
    '''
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write_to_file(file_path, content):
    '''
    A function to standardize file write operations.
    '''
    with open(file_path, 'w') as file:
        file.write(content)


def remove_punctuation(input_string):
    '''
    A function to remove punctuation from a string.
    '''
    return re.sub(r'[^\w\s]', '', input_string)


def convert_to_lowercase(input_string):
    '''
    A function to convert a string to lowercase.
    '''
    return input_string.lower()


def convert_to_uppercase(input_string):
    '''
    A function to convert a string to uppercase.
    '''
    return input_string.upper()

