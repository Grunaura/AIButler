import argparse
import nltk
import spacy  # Import the Spacy library
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

# Add the new function for named entity recognition
def perform_ner(text):
    """Perform named entity recognition on the text using Spacy."""
    # Load the English model from Spacy
    nlp = spacy.load('en_core_web_sm')

    # Process the text
    doc = nlp(text)

    # Extract entities and their types
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some text.')
    parser.add_argument('text', type=str, help='The text to process')

    args = parser.parse_args()

    processed_text = process_text(args.text)
    ner_results = perform_ner(args.text)
    
    print("Processed Text:", processed_text)
    print("NER Results:", ner_results)
