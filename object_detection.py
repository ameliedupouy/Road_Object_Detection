import torch
import cv2
import os
from pathlib import Path

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # use YOLOv5 for object detection

INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# colors for each object
COLORS = {
    "person": (204, 229, 255),
    "bicycle": (255, 204, 204),
    "car": (204, 255, 204),
    "motorcycle": (255, 229, 204),
    "bus": (255, 255, 204),
    "truck": (229, 204, 255),
    "traffic light": (153, 255, 255),
    "default": (240, 240, 240)  # for other objects such as bench
}


def detection_and_annotation(image_path, output_path):
    image = cv2.imread(image_path)  # charge the image

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = model(image_rgb)  # object detection
    detections = results.xyxy[0]  # list detected objects
    inventory = []  # stock detected objects

    for *box, confidence, class_id in detections:  # annotations
        x1, y1, x2, y2 = map(int, box)
        label = model.names[int(class_id)]
        color = COLORS.get(label, COLORS["default"])

        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)  # draw a rectangle around the object

        # text
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(image, (x1, y1 - text_height - baseline), (x1 + text_width, y1), color, -1)
        cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        width = x2 - x1  # inventory
        height = y2 - y1
        inventory.append({
            "label": label,
            "position": (x1, y1, x2, y2),
            "size": (width, height)
        })

    print("\nObjects detected:")
    for item in inventory:
        print(f"Object : {item['label']}, "
              f"Position : {item['position']}, "
              f"Size : {item['size']}")

    cv2.imwrite(output_path, image)  # save the image with annotations

    return image


def display_image(image, title):
    cv2.imshow(title, image)  # show the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # close the window


def process_single_image():
    images = sorted(Path(INPUT_FOLDER).glob('*.png')) + sorted(Path(INPUT_FOLDER).glob('*.jpg'))

    if not images:
        print("No valid images found in the input folder.")
        return

    image_dict = {img.stem: img for img in images}

    ##print("\nAvailable images:")
    ##for idx, img_stem in enumerate(image_dict, 1):
    ##    print(f"{idx}. {img_stem}")

    image_num = input("\nEnter the number (or name) of the image to process: ").strip()  # choose an image by its number

    try:
        image_num = int(image_num) - 1  # convert to index
        image_path = list(image_dict.values())[image_num]
    except (ValueError, IndexError):
        print("Invalid number. Please enter a valid image number.")
        return

    output_path = os.path.join(OUTPUT_FOLDER, image_path.name)
    print(f"Processing: {image_path} -> {output_path}")

    annotated_image = detection_and_annotation(str(image_path), output_path)


    display_image(annotated_image, "Annotated Image")


def process_all_images():
    images = sorted(Path(INPUT_FOLDER).glob('*.png')) + sorted(Path(INPUT_FOLDER).glob('*.jpg'))

    if not images:
        print("No valid images found in the input folder.")
        return

    print(f"\nProcessing {len(images)} images...")

    for image_path in images:
        output_path = os.path.join(OUTPUT_FOLDER, image_path.name)
        print(f"Processing: {image_path} -> {output_path}")


        annotated_image = detection_and_annotation(str(image_path), output_path)

    print(f"\nAll images have been processed. You can find the annotated images in the '{OUTPUT_FOLDER}' folder.")


if __name__ == "__main__":
    choice = input("Do you want to process (1) a single image or (2) all images? Enter 1 or 2: ")

    if choice == '1':
        process_single_image()
    elif choice == '2':
        process_all_images()
    else:
        print("Invalid choice. Please enter 1 or 2.")
