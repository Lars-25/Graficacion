import cv2 as cv
import numpy as np

# Canvas
img = np.zeros((500, 500), np.uint8)

cv.circle(img, (250, 250), 100, (255, 255, 0), -1)  # Círculo azul
cv.imshow('Canvas', img)


# Calcular el centroide
i = 0
j = 0

while(img [i , j] == 0):
    if (i == 500):
        i = 0
        j += 1

print(i,j)

cv.waitKey(0)
cv.destroyAllWindows()
