import sys
import re
import os
from PIL import Image

#Grab first and second argument
folder1 = sys.argv[1]
folder2 = sys.argv[2]

pattern = re.compile(r'\D+\/')
valid1 = pattern.match(folder1)
valid2 = pattern.match(folder2)

if valid1 and valid2:
    print('format is correct')
else:
    print('Arguments must end with / to denote folders')

#Check if new folder exist if not create it
if not os.path.exists(folder2):
    os.mkdir(folder2)

#Loop through Pokedex
img_list = os.listdir(folder1)

for item in img_list:
    img = Image.open(f'{folder1}{item}')
    filename = os.path.splitext(item)[0]
    img.save(f'{folder2}{filename}.png', 'png')





