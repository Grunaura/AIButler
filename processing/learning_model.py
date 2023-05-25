from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from processing.text_processing import process_text
from gensim.models import Word2Vec  # Import the Gensim library
import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
import os

BUFFER_SIZE = 20000
BATCH_SIZE = 64
MAX_LENGTH = 50

# Loading the data
data = tfds.load(name='tiny_shakespeare', split='train')
data = data.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

def create_model(vocab_size, embedding_dim, units):
    """Creates and returns a transformer model."""
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim),
        tf.keras.layers.GRU(units, return_sequences=True),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model

def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

def train_model(dataset, model, epochs=10):
    """Trains the model on the provided training data."""
    model.compile(optimizer=Adam(), loss=loss)
    model.fit(dataset, epochs=epochs)

def generate_text(model, start_string):
    """Generates text using the trained model."""
    # Convert the start string to numbers
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    temperature = 1.0

    model.reset_states()
    for i in range(1000):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)

        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))

# Add the new function for training a Word2Vec model
def train_word2vec_model(sentences):
    """Train a Word2Vec model with the provided sentences using Gensim."""
    try:
        model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        model.train(sentences, total_examples=len(sentences), epochs=10)
        return model
    except Exception as e:
        print(f"An error occurred while training the Word2Vec model: {e}")

if __name__ == "__main__":
    vocab = sorted(set(data))
    char2idx = {u:i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab
