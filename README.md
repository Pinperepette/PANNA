# PANNA - Dog Breed Recognition

## Overview

**PANNA** is a Python script designed to recognize the breed of a dog from an image. The name "PANNA" is not just a reference to a beloved Maremma Sheepdog, but also an acronym derived from the key libraries used in the script:

- **P**: Pillow - for image processing
- **A**: Albumentations - for image augmentation
- **N**: NumPy - for numerical operations
- **N**: Neural Networks (via PyTorch) - for model inference
- **A**: Argparse - for command-line argument parsing

The script utilizes a pre-trained ResNet50 model to predict the dog's breed and provides the result directly in the console.

## Requirements

To run this script, you need to have Python 3.7 or later installed on your system. Additionally, the following Python libraries are required:

- numpy
- pillow
- albumentations
- torch
- torchvision
- argparse

You can install these dependencies using pip:

```bash
pip install numpy pillow albumentations torch torchvision argparse
```

## Usage


1. **Run the Script**

   To use the script, run the following command in your terminal:

   ```bash
   python PANNA.py /path/to/your/dog_image.jpg
   ```

   Replace `/path/to/your/dog_image.jpg` with the actual path to the image of the dog you want to analyze.

2. **Output**

   The script will output the predicted breed of the dog based on the input image. For example:

   ```
   Razza predetta: West Highland White Terrier
   ```

## Customization

If you want to adjust the script for different models or datasets, you can modify the `predict_breed` function and the way labels are loaded. The script currently uses the ResNet50 model pre-trained on ImageNet.

## License

This script is open-source and available under the MIT License.

## Credits

Created by [Your Name]. Inspired by a Maremma Sheepdog named Panna and powered by the PANNA libraries.
