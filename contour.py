from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.CONTOUR)

#  Mostra o contorno de toda imagem

img2.save('imagens/tucanocontour.jpg')