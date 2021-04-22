from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.BLUR)

#  Mostra uma imagem borada

img2.save('imagens/tucanoblur.jpg')