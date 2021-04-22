from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.EDGE_ENHANCE)

#  Realça a imagem

img2.save('imagens/tucanoedge_enhance.jpg')