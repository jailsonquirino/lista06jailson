from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.SMOOTH)

# A imagem fica suave

img2.save('imagens/tucanosmooth.jpg')