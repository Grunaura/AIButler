"""
This module provides a Vectorizer class that uses FAISS and Annoy for vector indexing and similarity search,
and Redis for vector caching. 

Written by: Adam Messick
Date: 5/24/2023
"""

# Import necessary libraries
import numpy as np
import redis
import faiss
from annoy import AnnoyIndex

try:
    # Establish a connection to Redis
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
except redis.ConnectionError as err:
    print(f"Error connecting to Redis: {err}")

class Vectorizer:
    def __init__(self, dim):
        self.dim = dim
        self.faiss_index = faiss.IndexFlatL2(dim)
        self.annoy_index = AnnoyIndex(dim, 'angular')
    
    def add_vector(self, vector_id, vector):
        # Add vector to faiss
        self.faiss_index.add(np.array([vector]))
        n = self.faiss_index.ntotal
        
        # Add vector to annoy
        self.annoy_index.add_item(n-1, vector)
        
        # Cache vector to Redis
        try:
            redis_client.hset('vectors', vector_id, vector.tobytes())
        except redis.RedisError as err:
            print(f"Error caching vector to Redis: {err}")

    def build_annoy_index(self, n_trees=10):
        try:
            self.annoy_index.build(n_trees)
        except Exception as err:
            print(f"Error building Annoy index: {err}")

    def get_vector(self, vector_id):
        # Retrieve vector from Redis
        try:
            vector_bytes = redis_client.hget('vectors', vector_id)
        except redis.RedisError as err:
            print(f"Error retrieving vector from Redis: {err}")
            return None
        
        if vector_bytes is None:
            return None
        else:
            vector = np.frombuffer(vector_bytes)
            return vector
