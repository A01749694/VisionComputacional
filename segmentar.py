import cv2
import numpy as np

captura = cv2.VideoCapture(0)

while True:
    # Captura de fotograma
    ret, fotograma = captura.read()

    # ROJO
    #lower = np.array([136, 87, 111])
    #upper = np.array([180, 255, 255])

    # AMARILLO
    #lower = np.array([20, 100, 100])
    #upper = np.array([30, 255, 255])

    # Verde
    lower = np.array([40, 40, 40])
    upper = np.array([80, 255, 255])

    #Blanco
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 55, 255])

    hsvFrame = cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvFrame, lower, upper)
    mask_white = cv2.inRange(hsvFrame, lower_white, upper_white)

    #Combinar las mascaras
    mask_combinada = cv2.bitwise_or(mask, mask_white)

    detected_output = cv2.bitwise_and(fotograma, fotograma, mask = mask_combinada)

    # Mostrar fotogramas
    cv2.imshow("Camara", detected_output)

    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y destruir las ventanas
captura.release()
cv2.destroyAllWindows()