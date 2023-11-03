from PIL import Image, ImageFilter
'''
Just a playground file for a Pillow library 
'''

img = Image.open('./Pokedex/pikachu.jpg')

filtered_image = img.filter(ImageFilter.BLUR)

# print(img)

filtered_image.save('bluredPicakhu.jpg','jpeg') 