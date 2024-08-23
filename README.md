
# PANNA - Dog Breed Recognition

## Overview

**PANNA** is a Python script designed to recognize the breed of a dog from an image. The name "PANNA" is not just inspired by a beloved Maremma Sheepdog, but also serves as an acronym representing the key libraries utilized in the script:

- **P**: Pillow - for image processing
- **A**: Albumentations - for image augmentation
- **N**: NumPy - for numerical operations
- **N**: Neural Networks (via PyTorch) - for model inference
- **A**: Argparse - for command-line argument parsing

The script uses a pre-trained ResNet50 model to predict the dog's breed and outputs the result directly in the console.

## Requirements

Ensure you have Python 3.7 or later installed. The required Python libraries are:

- numpy
- pillow
- albumentations
- torch
- torchvision
- argparse

You can install these dependencies with pip:

```bash
pip install numpy pillow albumentations torch torchvision argparse
```

## Usage

1. **Prepare the ImageNet Labels**

   The `imagenet_labels.txt` file, which contains the labels corresponding to the indices of ImageNet classes, is already included in the repository. Ensure this file is in the same directory as the `PANNA.py` script.

2. **Run the Script**

   To use the script, execute the following command in your terminal:

   ```bash
   python PANNA.py /path/to/your/dog_image.jpg
   ```

   Replace `/path/to/your/dog_image.jpg` with the actual path to the dog image you wish to analyze.

3. **Output**

   The script will output the predicted breed of the dog based on the input image. For example:

   ```
   Razza predetta: West Highland White Terrier
   ```

## License

This script is open-source and available under the MIT License.

