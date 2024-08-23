#!/usr/bin/env python

import numpy as np
from PIL import Image
import albumentations as A
import torch
from torchvision import models, transforms
import argparse


imagenet_labels = {idx: label for idx, label in enumerate(open("imagenet_labels.txt").read().splitlines())}

def load_and_preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image_np = np.array(image)
    
    transform = A.Compose([
        A.Resize(224, 224),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ])
    augmented = transform(image=image_np)
    
    image_tensor = torch.tensor(augmented['image'].transpose(2, 0, 1)).float().unsqueeze(0)
    return image_tensor


def predict_breed(image_tensor):
    model = models.resnet50(pretrained=True)
    model.eval()
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = outputs.max(1)
        return predicted.item()

def main(image_path):
    image_tensor = load_and_preprocess_image(image_path)
    breed_idx = predict_breed(image_tensor)
    breed_name = imagenet_labels[breed_idx]
    print(f"Razza predetta: {breed_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Riconoscimento della razza di un cane da un'immagine.")
    parser.add_argument("image_path", type=str, help="Percorso dell'immagine del cane.")
    
    args = parser.parse_args()
    main(args.image_path)

