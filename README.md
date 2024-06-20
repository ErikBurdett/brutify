# Metal Album Cover Style Image Converter

A Python script that takes an image and converts it to a high grain/contrast heavy metal album cover style, inspired by Burzum and similar bands.

## Fancy Description

This repository contains a script and instructions to transform a character portrait into a black and white grainy image typical of Burzum and other metal band album covers. The processed image maintains high detail while incorporating increased contrast and graininess to achieve the desired aesthetic. Should be able to process 20+ images of different times in each run, haven't hit a limit yet - though I'm sure there is one depending on the size of the input images. 

## License

This is a proprietary script, but free to use. Please use it as a reference and give credit if used in any production, product, publication, etc: [https://github.com/ErikBurdett/brutify](https://github.com/ErikBurdett/brutify)

## Example Images

**Input Image**

![Input Image](input_image.png)

**Output Image**

![Output Image](output_image.png)

## Files

- **input_image.png**: The original colored image to be transformed.
- **output_image.png**: The final black and white grainy image with enhanced contrast and details.

## Image Processing Steps

1. **Convert to Grayscale**:
   - The original colored image is converted to grayscale to fit the monochrome style typical of metal album covers.
2. **Enhance Contrast**:
   - The contrast of the grayscale image is significantly enhanced to create stark differences between light and dark areas, emphasizing the dramatic aesthetic.
3. **Increase Brightness**:
   - The image brightness is slightly increased to enhance the visibility of details while maintaining a dark, somber look.
4. **Add Graininess**:
   - Fine grain is added to the image to mimic the texture seen in many old, low-resolution black and white photographs. This step is carefully calibrated to maintain image details.
5. **Sharpen the Image**:
   - An unsharp mask filter is applied to enhance the edges and fine details within the image, ensuring that the final result retains clarity despite the added grain.

## Usage

To use or modify the image processing steps, follow the provided Python script utilizing the Pillow library:

```python
import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

# Function to add fine grain to an image
def add_fine_grain(image, amount=0.5):
    arr = np.array(image)
    noise = np.random.normal(0, 255 * amount, arr.shape).astype(np.int16)
    noisy_arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_arr)

# Function to process a single image
def process_image(image_path, output_path, output_reversed_path):
    try:
        # Load the image
        image = Image.open(image_path)

        # Convert to grayscale
        image_bw = ImageOps.grayscale(image)

        # Determine grain amount and enhancement levels based on resolution
        width, height = image.size
        if max(width, height) <= 1000:
            grain_amount = 0.1  # Reduced grain amount for lower resolution
            contrast_enhancement = 3.5
        else:
            grain_amount = 0.3  # Reduced grain amount for higher resolution
            contrast_enhancement = 5.0

        # Enhance the contrast significantly to deepen blacks
        enhancer = ImageEnhance.Contrast(image_bw)
        image_high_contrast = enhancer.enhance(contrast_enhancement)

        # Slightly increase the brightness to make the image brighter
        enhancer = ImageEnhance.Brightness(image_high_contrast)
        image_brightened = enhancer.enhance(1.1)  # Slightly increased brightness

        # Add graininess while keeping details
        image_grainy = add_fine_grain(image_brightened, amount=grain_amount)

        # Apply a strong sharpening filter to enhance details
        image_sharpened = image_grainy.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=3))

        # Save the final image
        image_sharpened.save(output_path)

        # Reverse black and white
        image_reversed = ImageOps.invert(image_sharpened)
        image_reversed.save(output_reversed_path)
    except Exception as e:
        print(f"Error processing file {image_path}: {e}")

# Function to find the next available iteration number
def get_next_iteration():
    iteration = 1
    while True:
        output_folder = f'output_{iteration}'
        output_reversed_folder = f'output_reversed_{iteration}'
        if not os.path.exists(output_folder) and not os.path.exists(output_reversed_folder):
            break
        iteration += 1
    return iteration

# Define input folder
input_folder = 'input'

# Get the next iteration number
iteration = get_next_iteration()

# Define output folders with iteration number
output_folder = f'output_{iteration}'
output_reversed_folder = f'output_reversed_{iteration}'

# Create output folders if they don't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(output_reversed_folder):
    os.makedirs(output_reversed_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):  # Added .webp to the list
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        output_reversed_path = os.path.join(output_reversed_folder, filename)
        process_image(input_path, output_path, output_reversed_path)

```

Replace input_image.png with the path to your input image file and output_image.png with the desired path for the output image file, then run the script to generate the styled image. Note that it can take multiple images of multiple types in one run - haven't hit a limit yet. 

### Requirements
Python 3.x
Pillow library
NumPy library
Install the required libraries using pip:

```bash

pip install pillow numpy
```
### License
This is a propietary script, but free to use - please use it as reference and give credit if used in any production, product, publication, etc: https://github.com/ErikBurdett/brutify