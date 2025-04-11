# Danae Troupe
# Last Updated: 4/11/2025

from PIL import Image, ImageOps
import os

EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

def addBorder(path, size, color, out, pre='border_'):
    image = Image.open(path)
    new_image = ImageOps.expand(image, border=size, fill=color)
    filename = os.path.basename(path)
    os.makedirs(out, exist_ok=True)
    new_image.save(f'{out}/{pre}{filename}')
    
def main():
    directory = input("Please select the folder with your files: ")
    color = input("Please type the color name (hit enter for 'white'): ") or 'white'
    size = input("Please type your border size (int) (or enter for default): ")
    size = int(size) if size else 10
    output = input("Type path to output directory (or enter for default): ") or './output'
    
    images = [f for f in os.listdir(directory) if f.lower().endswith(EXTENSIONS)]
    for image in images:
        addBorder(f'{directory}/{image}', size, color, output)
    print(f'Task complete. Files in {output}')
    
main()
    