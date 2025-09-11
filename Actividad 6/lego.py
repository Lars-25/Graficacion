# Ejemplo de lego con primitivas
import cv2 as cv
import numpy as np

# Definir el canvas
img = np.ones((500, 500, 3), np.uint8) # Imagen inicial con 3 canales

# Dibujar la cabeza amarilla (circulo con bordes redondeados)
cv.circle(img, (250, 150), 50, (0, 255, 255), -1)  # Cara



cv.imshow('Canvas', img)
cv.waitKey(0)
cv.destroyAllWindows()
