import os
import glob
from PIL import Image

if not os.path.exists('Grayscale_images'):
    os.makedirs('Grayscale_images')

images_jpg = glob.glob('*.jpg')
images_png = glob.glob('*.png')

for i in images_jpg:
    im = Image.open(i)
    grayscale = im.convert('L')
    grayscale.save('Grayscale_images\\' + 'Grayscale_' + i[:-4] + '.jpg')

for i in images_png:
    im = Image.open(i)
    grayscale = im.convert('L')
    grayscale.save('Grayscale_images\\' + 'Grayscale_' + i[:-4] + '.png')

grayscale_jpg = glob.glob(r'Grayscale_images\*.jpg')
grayscale_png = glob.glob(r'Grayscale_images\*.png')

jpg_converted = len(grayscale_jpg)
png_converted = len(grayscale_png)

print(
    f'You converted {jpg_converted} jpgs and {png_converted} pngs to grayscale.')
