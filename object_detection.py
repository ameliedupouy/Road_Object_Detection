import os
import cv2
import torch
from pathlib import Path
import matplotlib.pyplot as plt


## à ajouter : affichage de l'image avant et après

# Initialisation du modèle pré-entraîné YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # YOLOv5s pour rapidité

# Dossiers de travail
INPUT_FOLDER = 'input_images'  # Chemin des images à analyser
OUTPUT_FOLDER = 'output_images'  # Chemin pour sauvegarder les images annotées

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def detect_and_annotate(image_path, output_path):
    # Chargement de l'image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Détection des objets
    results = model(image_rgb)
    detections = results.xyxy[0]  # Coordonnées des cadres détectés

    # Annoter chaque détection
    for *box, confidence, class_id in detections:
        x1, y1, x2, y2 = map(int, box)
        label = f"{model.names[int(class_id)]} {confidence:.2f}"

        # Dessiner le cadre et l'étiquette
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Cadre vert
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Sauvegarder l'image annotée
    cv2.imwrite(output_path, image)

    # Afficher l'image annotée
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Image Annotée")
    plt.axis("off")
    plt.show()

def process_images():
    # Traiter chaque image dans le dossier d'entrée
    for img_file in Path(INPUT_FOLDER).glob('*'):
        output_path = os.path.join(OUTPUT_FOLDER, img_file.name)
        print(f"Traitement : {img_file} -> {output_path}")
        detect_and_annotate(str(img_file), output_path)

if __name__ == "__main__":
    process_images()