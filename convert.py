import os
from PIL import Image

# Path to the folder containing images
folder_path = 'convert'

# Supported image formats (you can add more formats if needed)
supported_formats = ('.png', '.webp', '.bmp', '.gif', '.tiff', '.jpeg', '.jpg')

# Create the output directory if it doesn't exist
output_folder = os.path.join(folder_path, 'jpeg_output')
os.makedirs(output_folder, exist_ok=True)

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(supported_formats):
        # Full path to the image file
        file_path = os.path.join(folder_path, filename)
        
        # Open the image using PIL
        with Image.open(file_path) as img:
            # Convert the image to RGB (necessary for non-RGB formats like PNG with transparency)
            rgb_img = img.convert('RGB')
            
            # Build the output file path with a .jpeg extension
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpeg")
            
            # Save the image as JPEG with maximum quality
            rgb_img.save(output_file_path, 'JPEG', quality=95)

print(f"Conversion complete. All images saved in {output_folder}")
