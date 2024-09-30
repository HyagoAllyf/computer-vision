'''
import cv2

tomar cuidado com as barras

imagem = cv2.imread('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/livro-visao-computacional-master/imagens/cap01/001.png')
cv2.imshow('Imagem', imagem) # titulo da imagem
cv2.waitKey(0)
cv2.destroyAllWindows()

Ler videos

captura = cv2.VideoCapture('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/pythonProject2/video/escalator.mp4')


while True:
    ret, frame = captura.read()
    cv2.imshow('Imagem', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

captura.relase()
cv2.destroyAllWindows()

captura de webcam


'''
