from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)

#  Deixa a imagem com mais realce

img2.save('imagens/tucanoedge_enhance_more.jpg')