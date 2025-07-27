# Card Prediction Application

A simple machine learning application that uses a Convolutional Neural Network (CNN) models trained on images of playing cards and predicts the card type from an uploaded image.

Models are trained in notebook files, and the trained model is saved in the `model` directory. The application uses TensorFlow for image processing, prediction and Flask for the web interface.

## Setup Instructions

### Prerequisites
- Conda (Anaconda or Miniconda)
- Python 3.9
- NVIDIA GPU (optional, for faster training and inference)
- CUDA toolkit and cuDNN (if using GPU)

### Cloning the Repository

Clone the repository and navigate to the project directory:
```bash
    git clone https://github.com/pirrozani/Card-Prediction-Application.git && cd Card-Prediction-Application
```

### Downloading the Dataset

> [!NOTE]
> This step is necessary only if you want to train the model yourself.
> If you want to use the pre-trained model, you can skip this step and directly run the application.

To download the dataset, follow these steps:
1. Go to the Kaggle dataset page [Cards Image Dataset-Classification](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification/data).
2. Click on the "Download" button to download the dataset as a ZIP file.
3. Extract the ZIP file to a directory of your choice.
4. Place the extracted dataset in the `data` directory of this project.


### Creating a Python Environment for TensorFlow GPU using Conda

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

### Running the Application

After setting up the environment, you can run the application by:

```
# Make sure you have activated the tf_gpu environment
conda activate tf_gpu

# Run the Flask web server
python main.py
```

### Using Docker
You can run the application in a Docker container instead of using conda. This is particularly useful if you want to avoid dependency issues or if you prefer a containerized environment.

#### Prerequisites for Docker
- Ensure Docker and Docker Compose are installed on your machine.
- If you want to use GPU acceleration, ensure that the NVIDIA Container Toolkit is installed.

#### Running with Docker
> [!IMPORTANT]
> Make sure you are in the project directory where the `docker-compose.yml` file is located.

Build the Docker image and run the services using Docker Compose command.
```bash
  docker-compose up --build
```
If you want to run the application in detached mode, you can use:
```bash
  docker-compose up -d
```

To check if the services are running, you can use:
```bash
  docker ps
```

> [!NOTE]
> - The Docker setup automatically mounts the `models` and `uploads` directories for persistence
> - GPU acceleration is enabled by default if NVIDIA Container Toolkit is available
> - The container uses CUDA 11.8 with cuDNN 8 for optimal TensorFlow GPU performance

#### Stop the Application
You can stop the services using:
```bash
  docker-compose down
```
### Access the Application
Once the server is running, you can access it through your web browser no matter if you used conda or Docker installation.
Open your web browser and navigate to:

**http://localhost:5000**
