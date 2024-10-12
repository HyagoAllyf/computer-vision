import cv2
import numpy as np

indiceFrame = totalVerticesAnterior = 0
valoresMedidos = np.zeros(7)
video = cv2.VideoCapture('C:/Users/hyago/documentos/Meusprojetos/python/computacao_visual/computer-vision/formas-geometricas-480.mov')

# Verifica se o vídeo foi aberto corretamente
if not video.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

while True:
    ret, frameRGB = video.read()

    # Verifica se o quadro foi lido corretamente
    if not ret:
        print("Não foi possível ler o quadro ou o vídeo terminou.")
        break  # Sai do loop se não conseguir ler o quadro

    # Converte o quadro para escala de cinza
    frameCinza = cv2.cvtColor(frameRGB, cv2.COLOR_RGB2GRAY)

    # Binariza a imagem
    ret, frameBinarizado = cv2.threshold(frameCinza, 127, 255, cv2.THRESH_BINARY)

    # Calcula o valor médio atual
    valorMedioAtual = int(cv2.mean(frameBinarizado)[0])

    if valorMedioAtual != 0:
        if valorMedioAtual == int(cv2.mean(valoresMedidos)[0]):
            # Detecta contornos
            contornos, hierarquia = cv2.findContours(
                frameBinarizado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
            )
            
            if contornos:
                objeto = contornos[0]
                perimetro = cv2.arcLength(objeto, True)
                poligono = cv2.approxPolyDP(objeto, 0.03 * perimetro, True)
                totalVertices = len(poligono)

                if totalVertices != totalVerticesAnterior:
                    totalVerticesAnterior = totalVertices
                    if totalVertices == 3:
                        print('Triângulo')
                    elif totalVertices == 4:
                        print('Quadrado')
                    elif totalVertices > 7:
                        print('Círculo')

        # Armazena o valor médio atual
        valoresMedidos[indiceFrame] = valorMedioAtual
        if indiceFrame == 6:
            indiceFrame = -1
        indiceFrame += 1

    # Mostra o vídeo
    cv2.imshow('video', frameRGB)

    # Sai do loop se 'q' for pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o vídeo e destrói as janelas
video.release()
cv2.destroyAllWindows()
