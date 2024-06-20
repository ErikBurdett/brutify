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
