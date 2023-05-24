"""
learning_model.py

This module provides a more complex machine learning model for text generation, 
using the Keras Sequential API to create a transformer-based generative model.

Functions:
- create_model(): Creates and returns a transformer model.
- train_model(model, X_train, y_train): Trains the model on the provided training data.
- generate_text(model, start_string): Generates text using the trained model.
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from processing.text_processing import process_text
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

if __name__ == "__main__":
    vocab = sorted(set(data))
    char2idx = {u:i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)

    text_as_int = np.array([char2idx[c] for c in data])
    char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

    sequences = char_dataset.batch(MAX_LENGTH+1, drop_remainder=True)

    def split_input_target(chunk):
        input_text = chunk[:-1]
        target_text = chunk[1:]
        return input_text, target_text

    dataset = sequences.map(split_input_target)

    model = create_model(vocab_size = len(vocab), embedding_dim=256, units=1024)
    train_model(dataset, model, epochs=30)
    print(generate_text(model, start_string="Enter some text here"))
