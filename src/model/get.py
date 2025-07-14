import os
import tensorflow as tf
from tensorflow.python.keras.models import load_model
from tensorflow.keras import layers
from tensorflow.keras.utils import custom_object_scope


def get_models_from_path(models_path)-> dict:
    """
    Load all models from the specified directory.
    """
    models = {}

    # Create a dictionary with all possible variants of BatchNormalization
    custom_objects = {
        'BatchNormalization': tf.keras.layers.BatchNormalization,
        'batch_normalization': tf.keras.layers.BatchNormalization,
        'tensorflow.python.keras.layers.normalization.batch_normalization.BatchNormalization': tf.keras.layers.BatchNormalization,
        'tensorflow.python.keras.layers.normalization.BatchNormalization': tf.keras.layers.BatchNormalization,
        'tensorflow.keras.layers.BatchNormalization': tf.keras.layers.BatchNormalization,
        'keras.layers.BatchNormalization': tf.keras.layers.BatchNormalization,
        'keras.layers.normalization.batch_normalization.BatchNormalization': tf.keras.layers.BatchNormalization
    }

    for index, filename in enumerate(os.listdir(models_path)):
        if filename.endswith(".h5"):
            model_path = os.path.join(models_path, filename)
            try:
                # First attempt: Use the comprehensive custom object dictionary
                with custom_object_scope(custom_objects):
                    models[filename] = load_model(model_path)
                print(f"Successfully loaded model: {filename}")
            except Exception as e:
                print(f"Error loading model {filename}: {str(e)}")
                # Fall back to standard loading if custom objects fail
                try:
                    models[filename] = tf.keras.models.load_model(model_path, compile=False)
                    print(f"Loaded model without custom objects: {filename}")
                except Exception as e2:
                    print(f"Failed to load model even without custom objects: {str(e2)}")

    return models
