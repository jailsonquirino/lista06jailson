from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.SMOOTH_MORE)

#  A imagem fica mais suave

img2.save('imagens/tucanosmooth_more.jpg')