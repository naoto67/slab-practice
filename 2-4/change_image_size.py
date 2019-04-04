import sys
from PIL import Image

args = sys.argv

if len(args) != 4:
    print("引数が足りません")
    sys.exit(1)

image_name = args[1]
width = args[2]
height = args[3]

try:
    image = Image.open(image_name)
    resized_image = image.resize((int(width), int(height)))
    resized_image.save(image.filename)
except Exception as e:
    print(e)

