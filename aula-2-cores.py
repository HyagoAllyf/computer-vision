'''
import cv2

# Carregando imagem RGB e segmentando canais
imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')
azul, verde, vermelho = cv2.split(imagem)

# Exibindo imagens dos canais separados
cv2.imshow('Canal R', vermelho)
cv2.imshow('Canal G', verde)
cv2.imshow('Canal B', azul)

# Salvando imagens dos canais separados

cv2.imwrite('frutas-canal-vermelho.jpeg', vermelho)
cv2.imwrite('frutas-canal-verde.jpeg', verde)
cv2.imwrite('frutas-canal-azul.jpeg', azul)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Mesclar as cores

imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')

azul, verde, vermelho = cv2.split(imagem)

# combinando os três canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow('Imagem', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

# convertendo imagens em RGB para tons de cinza

# Carregando a imagem em RGB
imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')

# Convertendo e exibindo a imagem em tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
cv2.imshow('Imagem', imagem)
cv2.imshow('Imagem_cinza', imagem_cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()


imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matriz, saturado, valor = cv2.split(imagem)

cv2.imshow('Canal H', matriz)
cv2.imshow('Canal S', saturado)
cv2.imshow('Canal V', valor)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Combinando os canais em uma imagem HSV

imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matriz, saturacao, valor = cv2.split(imagem)

cv2.imshow('Canal H', matriz)
cv2.imshow('Canal S', saturacao)
cv2.imshow('Canal V', valor)

imagem = cv2.merge((matriz, saturacao, valor))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

cv2.imshow('Imagem', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''







