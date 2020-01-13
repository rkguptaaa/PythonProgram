from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.png')
img.show()
filtered_image = img.filter(ImageFilter.BLUR)

filtered_image.save('pikachu_blur.png', 'png')
filtered_image.show()