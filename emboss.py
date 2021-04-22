from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.EMBOSS)

# Imagem em relevo

img2.save('imagens/tucanoemboss.jpg')