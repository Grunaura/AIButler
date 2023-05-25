"""
    Author: Adam Messick
    Date: 5/24/2023
    process_options.py
"""

import json

class ProcessOptions:
    def __init__(self):
        self.default_options = {
            "temperature": 0.7,
            "max_tokens": None,
            "top_p": None,
            "frequency_penalty": None,
            "presence_penalty": None,
            "max_length": None,
            "min_length": None,
            "seed": None,
            "stop_sequences": None,
            "num_responses": None,
            "echo": None,
            "clean_output": None,
            "content_rating": None,
            "language": None,
            "model": None,
            "format": None,
            "speed": None,
        }

    def process_options(self, options):
        options = json.loads(options)

        # Validate each option
        for key, value in options.items():
            if key not in self.default_options:
                raise ValueError(f"Invalid option: {key}")
            
            if key in ['temperature', 'top_p', 'frequency_penalty', 'presence_penalty', 'speed'] and (value < 0 or value > 1):
                raise ValueError(f"Invalid value for {key}: Must be between 0 and 1")

            if key in ['max_tokens', 'max_length', 'min_length', 'seed', 'num_responses'] and (not isinstance(value, int) or value < 0):
                raise ValueError(f"Invalid value for {key}: Must be a positive integer")
            
            if key == 'stop_sequences' and not isinstance(value, list):
                raise ValueError("Invalid value for stop_sequences: Must be a list")
            
            if key in ['echo', 'clean_output'] and not isinstance(value, bool):
                raise ValueError(f"Invalid value for {key}: Must be a boolean")

            if key == 'content_rating' and value not in ['G', 'PG', 'R']:
                raise ValueError("Invalid value for content_rating: Must be 'G', 'PG', or 'R'")
            
            if key == 'format' and value not in ['JSON', 'plain_text']:
                raise ValueError("Invalid value for format: Must be 'JSON' or 'plain_text'")
        
        # Merge default options with user options
        merged_options = {**self.default_options, **options}
        return merged_options
