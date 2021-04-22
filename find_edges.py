from PIL import Image, ImageFilter

img1 = Image.open('imagens/tucano.jpg')

img2 = img1.filter(ImageFilter.FIND_EDGES)

#  Mostra as bordas da imagem

img2.save('imagens/tucanofind_edges.jpg')