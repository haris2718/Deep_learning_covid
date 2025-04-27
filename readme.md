#  Chest X-ray Analysis for COVID-19 Diagnosis Using Deep Learning

##  Introduction

This project focuses on the **analysis of chest X-rays** with the goal of **classifying them into three distinct categories**: healthy patients, COVID-19 patients, and patients with common pneumonia. We employed **Deep Learning** methodologies using **TensorFlow/Keras**, specifically building a **Convolutional Neural Network (CNN)** based on the VGG16 architecture. 

The **training process** involved several steps: initially, the images underwent **preprocessing**, including pixel value **normalization** and data **augmentation**, which enhanced dataset diversity through rotations, shifts, and zoom transformations. These techniques help mitigate **overfitting**, where a model memorizes the training data but performs poorly on unseen examples.

During training, we implemented **dropout layers** (randomly disabling neurons), **learning rate scheduling**, and leveraged **pre-trained weights** from ImageNet (transfer learning) to achieve faster convergence and improved generalization. We also used callbacks such as `ModelCheckpoint` and `ReduceLROnPlateau` for saving optimal models and automatic learning rate adjustments. Evaluation metrics included **accuracy**, **loss**, and **validation accuracy**, which were tracked and visualized throughout training.

Finally, the model can **store optimal parameters** in a **CSV file**, and supports **easy customization** through adjustable parameters like learning rate, batch size, and number of epochs. This approach aims to create a tool that can **assist in automatic diagnosis** and **support medical personnel**, especially under the strain of a pandemic like COVID-19.

##  Project Overview

This subsystem is part of a broader deep learning initiative for **disease diagnosis from chest X-rays**. The developed model classifies X-rays into three categories:

-  Healthy
-  COVID-19 Patient
-  Pneumonia Patient

It leverages state-of-the-art artificial intelligence techniques and builds upon pre-trained models like **VGG16**.

---

##  Technologies

- **Python**
- **TensorFlow & Keras** (Deep Learning)
- **OpenCV** (Image Processing)
- **Pandas & NumPy** (Data Handling)
- **Matplotlib** (Visualization)
- **Google Colab / Google Drive** (Execution and Storage)

---

##  Features

### 1. Data Preprocessing

- **Normalization** of images (rescaling pixel values to [0,1])
- **Data Augmentation** using `ImageDataGenerator`:
  - Rotation, shifting, zooming, shearing
  - Overfitting reduction by image transformations
- Splitting data into **training** and **validation sets** with balanced categories

### 2. Model Development

- Based on **VGG16** with ImageNet weights (`include_top=False`)
- Initial model layers are **frozen** to retain pre-learned features
- Added fully connected (Dense) layers and dropout for overfitting prevention
- Final layer uses **softmax** for three-class classification

### 3. Training & Evaluation

- Set batch size, number of epochs, validation split
- **Resume training** from existing weights (`load_weights`)
- Use of callbacks:
  - `ModelCheckpoint`: Saves best model based on validation accuracy
  - `ReduceLROnPlateau`: Automatically reduces learning rate on performance plateau
  - `LearningRateScheduler`: Progressive learning rate adjustment
  - Custom Callback: Print training information, execution time, and accuracy gaps
- Learning Rate Scheduling via `lr_schedule` function
- Calculation of accuracy, precision, and recall

### 4. Saving & Reporting

- Save trained models in `saved_models_VGG16validation/`

- Visualize results with graphs:

  - Loss vs Validation Loss

  - Accuracy vs Validation Accuracy

- Save metrics to `.csv`

---

##  Data Structure

```bash
project/
├── extracted_files/
│   ├── train_images/              # Training images
│   ├── labels_train.csv           # Labels for the training set
│   └── saved_models_VGG16validation/
│       └── <saved_models>.h5
```

###  Prediction File with Pre-Trained Model

The `predict.ipynb` file loads the previously trained model, using saved weights from the best checkpoint, to classify chest X-rays into Healthy, Pneumonia, or COVID-19 categories. This evaluates the model’s ability to generalize to new, unseen data.

**Key Steps:**

- Load and evaluate the VGG16 + custom layers model
- Standardize test set images using `ImageDataGenerator`
- Extract predictions with softmax and save results to `.csv`
- Predictions include corresponding image ID and final class ID

**Output:**
A `.csv` file containing the final predictions, useful for further analysis or visualization.

---

###  Image Preprocessing - Padding Chest X-rays

The `image_folder_padding.py` script performs image preprocessing by applying **padding** to ensure all images have consistent dimensions, based on the largest image in the dataset. This is achieved using `OpenCV`, outputting the resized images to a separate folder.

 **Script Functions:**

- Detect the largest image (width & height) in the dataset
- Apply black padding (borders) so all images match the largest dimensions
- Center the original image within the new padded image
- Save the padded images to an `output_folder`

 **Why Padding is Important for Deep Learning:**

- Ensures **consistent input size** for CNNs
- **Preserves image aspect ratios** without distortion
- Helps the network **learn stable features** without being affected by varying image sizes

This preprocessing step is crucial, especially for medical X-ray datasets where **edge details** can have diagnostic significance.

