
# Road Object Detection Using YOLOv5

## Project Overview

This project, **Road Object Detection**, uses the **YOLOv5** (You Only Look Once) model to perform object detection on road-related images. The primary goal is to detect and annotate various objects, including cars, pedestrians, bicycles, trucks, and other vehicles.

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
├── input_images/        # Folder containing input images (.png, .jpg)  
├── output_images/       # Folder to save output (annotated) images  
├── venv/                # Virtual environment for the project  
├── README.md            # Project description and instructions  
├── object_detection.py  # Source code for object detection and annotation  

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

```bash
git clone https://github.com/ameliedupouy/Road_Object_Detection.git
cd Road_Object_Detection
```

### 2. Setting up the Virtual Environment:

If you haven't created the virtual environment yet, you can do so with the following command:

```bash
python -m venv venv
```

- On Windows:

  ```bash
  .venv\Scripts ctivate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies:

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install the necessary libraries manually:

```bash
pip install torch opencv-python
```

### 4. Running the Script:

Place the images you want to process inside the `input_images/` folder.  
Run the Python script:

```bash
python object_detection.py
```

When prompted, enter the number of the image to process. For example, type `1` to process the first image.

### Example Usage:

```bash
Enter the number of the image to process: 1
Processing: input_images/1.png -> output_images/1.png
```

## Performance Metrics

- **Accuracy**: The model detects common road objects such as vehicles and pedestrians with reasonable accuracy.
- **Speed**: The YOLOv5s model is optimized for speed and performs object detection in real-time.
- **Memory Efficiency**: YOLOv5s is smaller and faster, consuming less memory compared to other larger YOLO models.

## References and Documentation

- **YOLOv5**: The YOLOv5 model was used for object detection. [GitHub Repository](https://github.com/ultralytics/yolov5)
- **Torch**: The deep learning library used to load and run YOLOv5.
- **OpenCV**: An open-source computer vision library used for image manipulation and display.

## Issues and Contributions

### Known Issues:
- Only basic road objects are detected, such as vehicles and pedestrians.
- Real-time performance may vary based on hardware (CPU vs. GPU).

### How to Contribute:
- Fork the repository and submit a pull request to improve or extend functionality.
- Report issues or suggest features via the Issues tab on GitHub.

## Future Work

- **Add Additional Object Classes**: Extend the detection to include other objects such as traffic signs and road obstacles.
- **Improve Model Accuracy**: Fine-tune the model to improve detection accuracy for road objects.
- **Real-time Video Processing**: Implement real-time video object detection.
- **User Interface**: Develop a graphical interface for easier interaction.
