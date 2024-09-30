import cv2
'''
imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')
valorPixel = imagem[150,150]
print(f'{valorPixel} são valores em RGB(BGR)')
'''

imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
valorPixel = imagem[150, 150]
print(valorPixel)