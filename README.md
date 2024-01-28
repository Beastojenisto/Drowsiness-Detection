# Drowsiness Detection Model

Welcome to the Drowsiness Detection Model repository! This project includes a pre-trained Drowsiness Detector model, an Jupyter notebook with code to reproduce the model, the dataset used for training, and a Streamlit application (`app.py`) that showcases the model in action. The following sections provide an overview of the repository contents and instructions on how to use them.
## Streamlit Webapp

You can explore the Streamlit webapp associated with this project. Visit [Drowsiness Detector Webapp](https://huggingface.co/spaces/Beasto/DrowsinessDetectorYOLO) to experience the model in action.
## Repository Contents

1. **`DrowsinessDetector.pt`**: This is the pre-trained Drowsiness Detection model in PyTorch format.

2. **`drowsinessdetection.ipynb`**: The IPython notebook contains the code to reproduce and train the Drowsiness Detection model. Follow the step-by-step instructions in the notebook to understand and customize the training process.

3. **`Driver-Drowsiness-Detection`**: The `dataset` directory contains the dataset used for training the model. It includes labeled examples of images with and without signs of drowsiness.This is taken from roboflow from another person. You can go the the person's website from [HERE]([https://huggingface.co/spaces/Beasto/DrowsinessDetectorYOLO](https://universe.roboflow.com/augmented-startups/drowsiness-detection-cntmz)).

4. **`app.py`**: This python file contains the Streamlit application that allows users to interactively test the Drowsiness Detection model on their own images.

## Getting Started

To get started with the Drowsiness Detection Model, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/Drowsiness-Detection.git
2. **Navigate to the Repository:**
   ```bash
   cd Drowsiness-Detection
3. **Explore the code:**
   Open the drowsinessdetection.ipynb notebook to reporduce and train the model.
4. **Run the Streamlit Application**
   ```bash
   streamlit run app.py   
