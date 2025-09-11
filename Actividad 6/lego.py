# Ejemplo de lego con primitivas
import cv2 as cv
import numpy as np

# Definir el canvas
img = np.ones((1000, 1000, 3), np.uint8) # Imagen inicial con 3 canales

# Dibujar la cabeza amarilla (cuadrado)
cv.rectangle(img, (150, 150), (350, 350), (0, 255, 255), -1)  # Cara

# Dibujar los ojos (círculos)
cv.circle(img, (200, 200), 20, (0, 0, 0), -1)  # Ojo izquierdo
cv.circle(img, (300, 200), 20, (0, 0, 0), -1)  # Ojo derecho

# Dibujar la boca (línea)
cv.ellipse(img, (250, 250), (50, 50), 0, 0, 180, (0, 0, 0), -1)  # Boca

# Dibujar el cuerpo (rectángulo)
cv.rectangle(img, (100, 350), (405, 600), (0, 0, 255), -1)  # Cuerpo

# Dibujar los brazos (rectángulos)
cv.rectangle(img, (50, 350), (100, 650), (0, 0, 200), -1)  # Brazo izquierdo
cv.rectangle(img, (400, 350), (450, 650), (0, 0, 200), -1)  # Brazo derecho

# Dibujar las manos (círculos)
cv.circle(img, (75, 650), 30, (0, 255, 255), -1)  # Mano izquierda
cv.circle(img, (425, 650), 30, (0, 255, 255), -1)  # Mano derecha

# Dibujar las piernas (rectángulos)
cv.rectangle(img, (150, 600), (100, 900), (255, 0, 0), -1)  # Pierna izquierda
cv.rectangle(img, (400, 600), (350, 900), (255, 0, 0), -1)  # Pierna derecha



cv.imshow('Canvas', img)

# Dibuj

cv.waitKey(0)
cv.destroyAllWindows()
