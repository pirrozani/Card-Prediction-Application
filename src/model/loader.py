import os
from tensorflow.keras.models import load_model
from get import get_models_from_path

def model(model_name):
    models_path = "model"
    models = get_models_from_path(models_path)

    if model_name not in models:
        raise ValueError(f"Model '{model_name}' not found in the directory '{models_path}'")

    model_path = os.path.join(models_path, models[model_name])
    return load_model(model_path)