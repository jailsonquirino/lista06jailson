from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.SHARPEN)

#  Deixa a imagem mais afiada

img2.save('imagens/tucanosharpen.jpg')