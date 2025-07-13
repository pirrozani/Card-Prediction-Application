import os
from tensorflow.python.keras.models import load_model


def get_models_from_path(models_path)-> dict:
    """
    Load all models from the specified directory.
    """
    models = {}
    for index, filename in enumerate(os.listdir(models_path)):
        if filename.endswith(".h5"):
            model_path = os.path.join(models_path, filename)
            models[filename] = load_model(model_path)

    return models
