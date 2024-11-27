# Road Object Detection 

## Project Overview

This project, **Road Object Detection**, uses the **YOLOv5** (You Only Look Once) model to perform object detection on road-related images. The primary goal is to detect and annotate various objects, including cars, pedestrians, bicycles, traffic lights, trucks, and other vehicles.

### Key Objectives:
- **Object Detection**: Detect and annotate objects in road-related images using YOLOv5.
- **Image Annotation**: Annotate the detected objects with bounding boxes and labels.
- **Easy Image Selection**: Users can select and process images by entering their corresponding number.

### Results:
- The system accurately detects common road objects in images.
- Annotated images are saved in the output directory with object bounding boxes and labels.

## Source Code

### File Structure:
/Road_Object_Detection      
├── input_images  
├── output_images  
├── venv/   
├── README.md   
├── object_detection.py   


### Code Overview:
- **object_detection.py**: The main script for detecting and annotating objects using YOLOv5.
- **select_and_display_image()**: Lets users choose an image by entering a number, then displays both the original and annotated images.
- **detection_and_annotation()**: Detects and annotates objects in images with YOLOv5.
- **display_image()**: Displays the image using OpenCV.

### Dependencies:
- **Python 3.6+**
- **torch** (for YOLOv5)
- **opencv-python** (for image manipulation and display)
- **pathlib** (for managing file paths)

If you are using a virtual environment (`venv`), ensure that it is activated before installing dependencies.

---

## Installation and Usage

### 1. Setting up the Project:

Clone this repository to your local machine:


