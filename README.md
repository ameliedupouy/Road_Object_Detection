
# Road Object Detection

## Project Overview

This project, **Road Object Detection**, uses the Deap Learning **YOLOv5** (You Only Look Once) model to perform object detection on road-related images. The primary goal is to detect and annotate various obstacles on the road such as traffic lights, different types of vehicles, pedestrians and bicycles, to create an object detection system that can be used in automotive assistance systems to improve road safety.

### Key Objectives:
- **Object Detection**: Detect and annotate objects in road-related images using YOLOv5.
- **Image Annotation**: Annotate the detected objects with bounding boxes and labels.
- **Easy Image Selection**: Users can select and process images by entering their corresponding number.
- **Inventory**: Take inventory of the detected objects.

### Results:
- The system accurately detects common road objects in images.
- Annotated images are saved in the output directory with object labels.
- The inventory of detected objects is displayed in the console.

## Source Code

### File Structure:

```bash
/Road_Object_Detection
├── input_images/        # Folder containing input images (.png, .jpg)  
├── output_images/       # Folder to save output (annotated) images  
├── venv/                # Virtual environment for the project  
├── README.md            # Project description and instructions  
├── object_detection.py  # Source code for object detection and annotation  
```

### Code Overview:
- **object_detection.py**: The main script for detecting and annotating objects using YOLOv5.
- **select_and_display_image()**: Lets users choose an image by entering a number, then displays both the original and annotated images.
- **detection_and_annotation()**: Detects and annotates objects in images with YOLOv5 and take the inventory.
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

```bash
git clone https://github.com/ameliedupouy/Road_Object_Detection.git
cd Road_Object_Detection
```

### 2. Setting up the Virtual Environment:

If you haven't created the virtual environment yet, you can do so with the following command:

```bash
python -m venv venv
```

On **Windows**:

```bash
.venv\Scripts ctivate
```

On **macOS/Linux**:

```bash
source venv/bin/activate
```

### 3. Install Dependencies:

Install the required libraries, including Torch, OpenCV, and YOLOv5:

Install **Torch** and **OpenCV** using pip:

```bash
pip install torch torchvision opencv-python
```

Clone the **YOLOv5** repository and install its dependencies:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..
```

### 4. Running the Script:
You will find images for testing in the `input_images/` folder. You can also test with other images by placing them in the `input_images/` folder.

Run the Python script:

```bash
python object_detection.py
```

When prompted, enter the number (or the name) corresponding to the image you want to process.

#### Example Usage:

```bash
Enter the number of the image to process: 1
Processing: input_images/1.png -> output_images/1.png
```

The script will display the original image, process it, annotate it, and save the annotated image in the `output_images/` folder.


## Performance Metrics

| Metric                            | Value        |
|-----------------------------------|--------------|
| Accuracy                          | 80%          |
| Average Processing Time per Image | 0.12 seconds |
| Memory Usage                      | 7.58 MB       |

## References and Documentation

- **YOLOv5**: The YOLOv5 model was used for object detection. [GitHub Repository](https://github.com/ultralytics/yolov5)
- **Torch**: The deep learning library used to load and run YOLOv5.
- **OpenCV**: An open-source computer vision library used for image manipulation and display.

## Issues and Contributions

### Known Issues:
- Only basic road objects are detected, such as different types of vehicle, traffic lights and pedestrians.
- Real-time performance may vary based on hardware (CPU vs. GPU).

### How to Contribute:
- Fork the repository and submit a pull request to improve or extend functionality.
- Report issues or suggest features via the Issues tab on GitHub.

## Future Work

- **Add Additional Object Classes**: Extend the detection to include other objects such as road signs.
- **Real-time Video Processing**: Implement real-time video object detection.

