# Card Prediction Application

A simple machine learning application that uses a Convolutional Neural Network (CNN) models trained on images of playing cards and predicts the card type from an uploaded image.

Models are trained in notebook files, and the trained model is saved in the `model` directory. The application uses TensorFlow for image processing, prediction and Flask for the web interface.

## Setup Instructions

### Prerequisites
- Conda (Anaconda or Miniconda)
- Python 3.9
- Downloaded dataset from Kaggle


### Downloading the Dataset

The dataset was downloaded from Kaggle:

[Cards Image Dataset-Classification](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification/data).


### Creating a Python Environment for TensorFlow GPU

Follow these steps to set up a Python environment with GPU support for TensorFlow:

```
# Create a new conda environment with Python 3.9
conda create -n tf_gpu python=3.9

# Activate the environment
conda activate tf_gpu

# Install CUDA toolkit and cuDNN for GPU acceleration
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

# Upgrade pip
python -m pip install --upgrade pip

# Install required packages from `requirements.txt`
pip install -r requirements.txt
```

## Running the Application

After setting up the environment, you can run the application by:

```
# Make sure you have activated the tf_gpu environment
conda activate tf_gpu

# Run the Flask web server
python main.py
```

The web server will start, and you can access the application through your browser:


http://localhost:5000


