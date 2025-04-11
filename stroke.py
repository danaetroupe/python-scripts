# Danae Troupe
# Last Updated: 4/11/2025

from PIL import Image, ImageOps, ImageFilter
import os

EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

def addStroke(path, size, color, out, pre='stroke_'):
    image = Image.open(path).convert("RGBA")
    alpha = image.split()[3]
    # Create a solid color image with same size as alpha
    stroke_mask = ImageOps.expand(alpha, border=size, fill=0)
    
    # Blur + threshold to create an outline
    stroke_mask = stroke_mask.filter(ImageFilter.MaxFilter(size*2+1))

    # Create stroke image with desired color and mask
    stroke_image = Image.new("RGBA", stroke_mask.size, color)
    stroke_image.putalpha(stroke_mask)

    # Calculate offset to center the original image over the stroke
    offset = size, size
    final_image = Image.new("RGBA", stroke_mask.size, (0, 0, 0, 0))
    final_image.paste(stroke_image, (0, 0))
    final_image.paste(image, offset, mask=image)

    # Save image
    filename = os.path.basename(path)
    os.makedirs(out, exist_ok=True)
    final_image.save(f'{out}/{pre}{filename}')
    
def main():
    directory = input("Please select the folder with your files: ")
    color = input("Please type the color name (hit enter for 'white'): ") or 'white'
    size = input("Please type your border size (int) (or enter for default): ")
    size = int(size) if size else 10
    output = input("Type path to output directory (or enter for default): ") or './output'
    
    images = [f for f in os.listdir(directory) if f.lower().endswith(EXTENSIONS)]
    for image in images:
        addStroke(f'{directory}/{image}', size, color, output)
    print(f'Task complete. Files in {output}')
    
main()
    