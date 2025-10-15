import math

import cv2 as cv
import numpy as np


def aplicar_filtro_bilineal(imagen):
    """
    Aplica filtro bilineal con prioridad en vecinos:
    1. Primero intenta usar vecinos en CRUZ (arriba, abajo, izq, der)
    2. Si no hay vecinos en cruz, usa ESQUINAS
    """
    h, w = imagen.shape
    img_filtrada = imagen.copy().astype(np.float32)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if imagen[i, j] != 0:
                continue

            # Vecinos en cruz
            arriba = imagen[i - 1, j]
            abajo = imagen[i + 1, j]
            izquierda = imagen[i, j - 1]
            derecha = imagen[i, j + 1]

            # Vecinos en esquinas
            esquina_sup_izq = imagen[i - 1, j - 1]
            esquina_sup_der = imagen[i - 1, j + 1]
            esquina_inf_izq = imagen[i + 1, j - 1]
            esquina_inf_der = imagen[i + 1, j + 1]

            vecinos_cruz = []
            vecinos_esquina = []

            # Recolectar vecinos en cruz
            if arriba > 0:
                vecinos_cruz.append(float(arriba))
            if abajo > 0:
                vecinos_cruz.append(float(abajo))
            if izquierda > 0:
                vecinos_cruz.append(float(izquierda))
            if derecha > 0:
                vecinos_cruz.append(float(derecha))

            # Recolectar vecinos en esquinas
            if esquina_sup_izq > 0:
                vecinos_esquina.append(float(esquina_sup_izq))
            if esquina_sup_der > 0:
                vecinos_esquina.append(float(esquina_sup_der))
            if esquina_inf_izq > 0:
                vecinos_esquina.append(float(esquina_inf_izq))
            if esquina_inf_der > 0:
                vecinos_esquina.append(float(esquina_inf_der))

            if len(vecinos_cruz) > 0:
                valor_filtrado = sum(vecinos_cruz) / len(vecinos_cruz)
            elif len(vecinos_esquina) > 0:
                valor_filtrado = sum(vecinos_esquina) / len(vecinos_esquina)
            else:
                valor_filtrado = 0

            img_filtrada[i, j] = valor_filtrado

    return img_filtrada.astype(np.uint8)


def escalar_imagen(img, scale_x, scale_y):
    """Escala la imagen por factores scale_x y scale_y"""
    x, y = img.shape
    scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)
    for i in range(x):
        for j in range(y):
            scaled_img[i * scale_y, j * scale_x] = img[i, j]
    return scaled_img


def rotar_imagen(img, angle):
    """Rota la imagen angle grados alrededor del centro"""
    x, y = img.shape
    cx, cy = y // 2, x // 2
    theta = math.radians(angle)

    # Calcular nuevo tamaño para evitar recortes
    new_size = int(math.sqrt(x**2 + y**2)) + 1
    rotated_img = np.zeros((new_size, new_size), dtype=np.uint8)
    new_cx = new_cy = new_size // 2

    for i in range(x):
        for j in range(y):
            # Rotación alrededor del centro
            x_rel = j - cx
            y_rel = i - cy
            new_x = int(x_rel * math.cos(theta) - y_rel * math.sin(theta) + new_cx)
            new_y = int(x_rel * math.sin(theta) + y_rel * math.cos(theta) + new_cy)

            if 0 <= new_x < new_size and 0 <= new_y < new_size:
                rotated_img[new_y, new_x] = img[i, j]

    return rotated_img


def trasladar_imagen(img, dx, dy):
    """Desplaza la imagen dx píxeles en X y dy píxeles en Y"""
    x, y = img.shape
    translated_img = np.zeros((x, y), dtype=np.uint8)

    for i in range(x):
        for j in range(y):
            new_x = i + dy
            new_y = j + dx
            if 0 <= new_x < x and 0 <= new_y < y:
                translated_img[new_x, new_y] = img[i, j]

    return translated_img


# Cargar imagen original
img = cv.imread("Actividad Escalado/pokemon.png", 0)
if img is None:
    print("Error: No se pudo cargar la imagen")
    exit()

print("Imagen original cargada. Dimensiones:", img.shape)

# Ejercicio 1
print("\n=== Ejercicio 1 ===")
img_ej1 = escalar_imagen(img, 2, 2)
img_ej1 = aplicar_filtro_bilineal(img_ej1)
img_ej1 = rotar_imagen(img_ej1, 45)
img_ej1 = aplicar_filtro_bilineal(img_ej1)
print("Ejercicio 1 completado")

# Ejercicio 2
print("\n=== Ejercicio 2 ===")
img_ej2 = escalar_imagen(img, 2, 2)
img_ej2 = rotar_imagen(img_ej2, 45)
img_ej2 = aplicar_filtro_bilineal(img_ej2)
print("Ejercicio 2 completado")

# Ejercicio 3
print("\n=== Ejercicio 3 ===")
x, y = img.shape
# Trasladar al centro
cx, cy = x // 2, y // 2
img_ej3 = trasladar_imagen(img, cx, cy)
# Rotar 90 grados
img_ej3 = rotar_imagen(img_ej3, 90)
# Trasladar en 2 píxeles
img_ej3 = trasladar_imagen(img_ej3, 2, 2)
# Aplicar filtro bilineal
img_ej3 = aplicar_filtro_bilineal(img_ej3)
print("Ejercicio 3 completado")

# Mostrar resultados
cv.imshow("1. Original", img)
cv.imshow("2. Ejercicio 1", img_ej1)
cv.imshow("3. Ejercicio 2", img_ej2)
cv.imshow("4. Ejercicio 3", img_ej3)

cv.waitKey(0)
cv.destroyAllWindows()
