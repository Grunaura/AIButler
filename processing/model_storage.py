# model_storage.py
# Adam Messick
# Date: 2023-05-22

import joblib
import redis
from datetime import datetime

class ModelStorage:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def store_model(self, model, model_name, model_type):
        versioned_model_name = self._version_model_name(model_name)
        serialized_model = joblib.dumps((model, model_type))
        self.client.set(versioned_model_name, serialized_model)

    def retrieve_model(self, model_name):
        versioned_model_name = self._get_latest_version_model_name(model_name)
        if versioned_model_name is None:
            raise Exception(f"No stored versions found for model name: {model_name}")
        serialized_model = self.client.get(versioned_model_name)
        model, model_type = joblib.loads(serialized_model)
        return model, model_type

    def _version_model_name(self, model_name):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{model_name}:{timestamp}"

    def _get_latest_version_model_name(self, model_name):
        versioned_model_names = [k.decode() for k in self.client.keys() if k.decode().startswith(model_name)]
        if not versioned_model_names:
            return None
        return sorted(versioned_model_names, reverse=True)[0]


# Testing
if __name__ == "__main__":
    import sklearn.dummy
    model_storage = ModelStorage()
    dummy_model = sklearn.dummy.DummyClassifier()
    model_storage.store_model(dummy_model, 'dummy', 'sklearn')
    retrieved_model, model_type = model_storage.retrieve_model('dummy')
    print(f"Retrieved model of type: {model_type}")
