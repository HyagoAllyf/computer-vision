import cv2
imagem = imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap04/002.png')
imagem[150,150]=[250,250,250]
print(imagem[150,150])
cv2.imshow('imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()