"""
text_processing.py

This module provides functions for cleaning, tokenizing, and lemmatizing English text.

Functions:
- clean_text(text): Removes non-alphabetic characters and converts to lowercase.
- tokenize_text(text): Tokenizes the text into words.
- remove_stopwords(tokenized_text): Removes common English stopwords.
- lemmatize_text(tokenized_text): Lemmatizes the tokens (get the base form of each word).
- process_text(text): Performs all the above steps in order.
"""

import argparse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# If you haven't downloaded the necessary NLTK packages, uncomment and run the following lines:
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

def clean_text(text):
    """Remove non-alphabetic characters and convert to lowercase."""
    cleaned_text = ''.join([char for char in text if char.isalpha() or char.isspace()]).lower()
    return cleaned_text

def tokenize_text(text):
    """Tokenize the text into words."""
    tokenized_text = word_tokenize(text)
    return tokenized_text

def remove_stopwords(tokenized_text):
    """Remove common English stopwords."""
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in tokenized_text if word not in stop_words]
    return filtered_text

def lemmatize_text(tokenized_text):
    """Lemmatize the tokens (get the base form of each word)."""
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(word) for word in tokenized_text]
    return lemmatized_text

def process_text(text):
    """Perform all the above steps in order."""
    cleaned_text = clean_text(text)
    tokenized_text = tokenize_text(cleaned_text)
    filtered_text = remove_stopwords(tokenized_text)
    lemmatized_text = lemmatize_text(filtered_text)
    return lemmatized_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some text.')
    parser.add_argument('text', type=str, help='The text to process')

    args = parser.parse_args()

    processed_text = process_text(args.text)
    print(processed_text)
