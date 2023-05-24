# model_storage.py
# Author: Adam Messick
# Date: May 22, 2023

import pickle
import redis

class ModelStorage:

    def __init__(self):
        # Connect to local Redis instance
        self.redis_instance = redis.StrictRedis(host="localhost", port=6379, db=0)

    def store_model(self, model, model_name):
        try:
            # Use pickle to serialize the model object
            pickled_model = pickle.dumps(model)
            # Store the serialized model in Redis
            self.redis_instance.set(model_name, pickled_model)
            print(f"Model {model_name} stored successfully.")
        except Exception as e:
            print(f"An error occurred while storing the model: {e}")

    def retrieve_model(self, model_name):
        try:
            # Retrieve the serialized model from Redis
            pickled_model = self.redis_instance.get(model_name)
            # Use pickle to deserialize the model object
            model = pickle.loads(pickled_model)
            print(f"Model {model_name} retrieved successfully.")
            return model
        except Exception as e:
            print(f"An error occurred while retrieving the model: {e}")


# Test the ModelStorage class
if __name__ == "__main__":
    model_storage = ModelStorage()
    dummy_model = {"model": "This is a dummy model"}
    model_storage.store_model(dummy_model, "dummy_model")
    retrieved_model = model_storage.retrieve_model("dummy_model")
    print(retrieved_model)
