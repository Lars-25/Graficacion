import cv2 as cv
import numpy as np

# Definir el canvas
img = np.ones((500, 500, 3), np.uint8) * 255  # Imagen inicial con 3 canales


# .shape [alto, ancho, canales]

# Crear pong que rebote por el canvas (500 x 500) usando distacia euclidiana
pos_x, pos_y = 250, 250
vel_x, vel_y = 5, 5
radio = 5
while True:
    # Limpiar el canvas
    img[:] = 255

    # Dibujar la pelota
    cv.circle(img, (pos_x, pos_y), radio, (0, 0, 255), -1)

    # Actualizar posición
    pos_x += vel_x
    pos_y += vel_y

    # Rebotar en los bordes
    if pos_x - radio <= 0 or pos_x + radio >= img.shape[1]: # cambiar a img.shape[1] para ancho
        vel_x = -vel_x
    if pos_y - radio <= 0 or pos_y + radio >= img.shape[0]:
        vel_y = -vel_y
    # Mostrar el canvas
    cv.imshow('Pong', img)
    key = cv.waitKey(30)
    if key == 27:  # Esc para salir
        break
cv.destroyAllWindows()

