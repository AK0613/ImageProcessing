from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
#print(img.mode)
#filter
filtered_img = img.convert('L')
filtered_img.save("gray.png", "png")
#rotate
crooked = filtered_img.rotate(90)
crooked.save('crooked.png', 'png')
#resize
resize = filtered_img.resize((300, 300))
resize.save('resized.png', 'png')

#crop
box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
cropped.save('cropped.png', 'png')
#display
# filtered_img.show()
# crooked.show()
# resize.show()
# cropped.show()


img2 = Image.open('./Pokedex/astro.jpg')
print(img2.size)
img2.thumbnail((400,400))
img2.save('new_img.png', 'png')
print(img2.size)




