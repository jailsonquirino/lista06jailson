from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.DETAIL)

#  Mostra os detales da imagem 

img2.save('imagens/tucanodetail.jpg')