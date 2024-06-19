# README

## Metal Album Cover Style Image Converter

Lil python script that takes an image and converts it to a high grain/constrast heavy metal abum cover style, think Burzum, etc. 

Fancy Description:

This repository contains a script and instructions to transform a character portrait into a black and white grainy image typical of Burzum and other metal band album covers. The processed image maintains high detail while incorporating increased contrast and graininess to achieve the desired aesthetic.

### License
This is a propietary script, but free to use - please use it as reference and give credit if used in any production, product, publication, etc: https://github.com/ErikBurdett/brutify

### Files
- `input_image.png`: The original colored image to be transformed.
- `output_image.png`: The final black and white grainy image with enhanced contrast and details.

### Image Processing Steps

1. **Convert to Grayscale:**
   - The original colored image is converted to grayscale to fit the monochrome style typical of metal album covers.

2. **Enhance Contrast:**
   - The contrast of the grayscale image is significantly enhanced to create stark differences between light and dark areas, emphasizing the dramatic aesthetic.

3. **Darken the Image:**
   - The image brightness is reduced to give it a darker, more somber look.

4. **Add Graininess:**
   - Fine grain is added to the image to mimic the texture seen in many old, low-resolution black and white photographs. This step is carefully calibrated to maintain image details.

5. **Sharpen the Image:**
   - An unsharp mask filter is applied to enhance the edges and fine details within the image, ensuring that the final result retains clarity despite the added grain.

### Usage

To use or modify the image processing steps, follow the provided Python script utilizing the Pillow library:

```python
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

# Load the image
image_path = 'input_image.png'
image = Image.open(image_path)

# Convert to grayscale
image_bw = ImageOps.grayscale(image)

# Enhance the contrast significantly
enhancer = ImageEnhance.Contrast(image_bw)
image_high_contrast = enhancer.enhance(3.0)

# Darken the image to give it more of a metal album cover look
enhancer = ImageEnhance.Brightness(image_high_contrast)
image_dark = enhancer.enhance(0.5)

# Add graininess while keeping details
def add_fine_grain(image, amount=0.5):
    arr = np.array(image)
    noise = np.random.normal(0, 255 * amount, arr.shape).astype(np.int16)
    noisy_arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_arr)

image_grainy = add_fine_grain(image_dark, amount=0.2)

# Apply a slight sharpening filter to enhance details
image_sharpened = image_grainy.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

# Save the final image
output_path = 'output_image.png'
image_sharpened.save(output_path)
```

Replace input_image.png with the path to your input image file and output_image.png with the desired path for the output image file, then run the script to generate the styled image.

### Requirements
Python 3.x
Pillow library
NumPy library
Install the required libraries using pip:

```bash

pip install pillow numpy
Author
This image and processing script were created by [Your Name]. Feel free to reach out for any questions or further customizations.
```
### License
This is a propietary script, but free to use - please use it as reference and give credit if used in any production, product, publication, etc: https://github.com/ErikBurdett/brutify