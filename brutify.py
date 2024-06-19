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