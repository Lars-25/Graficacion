import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread("Actividad Escalado/goku.png", 0)
# Obtener el tamaño de la imagen
x, y = img.shape
# Definir el factor de escala
scale_x, scale_y = 2, 2
# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# Aplicar el escalado - Solo copiamos los píxeles originales
# Esto deja "huecos" entre los píxeles, rellenar con el filtro
for i in range(x):
    for j in range(y):
        scaled_img[i * 2, j * 2] = img[i, j]

print("Imagen escalada creada. Ahora aplicando filtro bilineal...")
print(f"Dimensiones: Original {img.shape} -> Escalada {scaled_img.shape}")


def aplicar_filtro_bilineal(imagen):
    """
    Aplica filtro bilineal con prioridad en vecinos:
    1. Primero intenta usar vecinos en CRUZ (arriba, abajo, izq, der) - peso 1
    2. Si no hay vecinos en cruz, usa ESQUINAS - peso 2

    Patrón de pesos:
    1   2   1      donde: 1 = cruz (prioridad)
    2   xy  2             2 = esquinas (secundario)
    1   2   1             xy = pixel a calcular
    """
    h, w = imagen.shape
    img_filtrada = imagen.copy().astype(np.float32)

    # Recorrer todos los píxeles (evitando bordes)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # Si el píxel ya tiene valor (no es cero/hueco), no lo modificamos
            if imagen[i, j] != 0:
                continue

            # Extraer vecindario 3x3 alrededor del píxel vacío
            # Posiciones:
            # [i-1,j-1]  [i-1,j]  [i-1,j+1]     esquina_sup_izq   arriba    esquina_sup_der
            # [i,j-1]    [i,j]    [i,j+1]    =  izquierda        CENTRO    derecha
            # [i+1,j-1]  [i+1,j]  [i+1,j+1]     esquina_inf_izq   abajo     esquina_inf_der

            # VECINOS EN CRUZ (eje x, y) - PRIORIDAD 1 - peso = 1
            arriba = imagen[i - 1, j]
            abajo = imagen[i + 1, j]
            izquierda = imagen[i, j - 1]
            derecha = imagen[i, j + 1]

            # VECINOS EN ESQUINAS - PRIORIDAD 2 - peso = 2
            esquina_sup_izq = imagen[i - 1, j - 1]
            esquina_sup_der = imagen[i - 1, j + 1]
            esquina_inf_izq = imagen[i + 1, j - 1]
            esquina_inf_der = imagen[i + 1, j + 1]

            # Listas para almacenar vecinos disponibles y sus pesos
            vecinos_cruz = []
            vecinos_esquina = []

            # Recolectar vecinos en CRUZ (peso 1)
            if arriba > 0:
                vecinos_cruz.append(float(arriba))
            if abajo > 0:
                vecinos_cruz.append(float(abajo))
            if izquierda > 0:
                vecinos_cruz.append(float(izquierda))
            if derecha > 0:
                vecinos_cruz.append(float(derecha))

            # Recolectar vecinos en ESQUINAS (peso 2)
            if esquina_sup_izq > 0:
                vecinos_esquina.append(float(esquina_sup_izq))
            if esquina_sup_der > 0:
                vecinos_esquina.append(float(esquina_sup_der))
            if esquina_inf_izq > 0:
                vecinos_esquina.append(float(esquina_inf_izq))
            if esquina_inf_der > 0:
                vecinos_esquina.append(float(esquina_inf_der))

            # Si hay vecinos en cruz, usar solo esos
            if len(vecinos_cruz) > 0:
                # SUMA de vecinos cruz / CANTIDAD de vecinos cruz
                suma_valores = sum(vecinos_cruz)
                cantidad_vecinos = len(vecinos_cruz)
                valor_filtrado = suma_valores / cantidad_vecinos

            # Si NO hay vecinos en cruz, usar esquinas
            elif len(vecinos_esquina) > 0:
                # SUMA de vecinos esquina / CANTIDAD de vecinos esquina
                suma_valores = sum(vecinos_esquina)
                cantidad_vecinos = len(vecinos_esquina)
                valor_filtrado = suma_valores / cantidad_vecinos

            else:
                # No hay vecinos, mantener en 0
                valor_filtrado = 0

            img_filtrada[i, j] = valor_filtrado

    return img_filtrada.astype(np.uint8)


def aplicar_filtro_bilineal_completo(imagen):
    """
    Alternativa: Usa TODOS los vecinos disponibles con sus pesos:
    - Vecinos en cruz: peso 1
    - Vecinos en esquinas: peso 2
    """
    h, w = imagen.shape
    img_filtrada = imagen.copy().astype(np.float32)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if imagen[i, j] != 0:
                continue

            # Extraer vecindario completo
            arriba = imagen[i - 1, j]
            abajo = imagen[i + 1, j]
            izquierda = imagen[i, j - 1]
            derecha = imagen[i, j + 1]

            esquina_sup_izq = imagen[i - 1, j - 1]
            esquina_sup_der = imagen[i - 1, j + 1]
            esquina_inf_izq = imagen[i + 1, j - 1]
            esquina_inf_der = imagen[i + 1, j + 1]

            # Calcular suma ponderada con TODOS los vecinos disponibles
            suma_valores = 0.0  # Usar float desde el inicio
            suma_pesos = 0

            # Vecinos en cruz (peso 1)
            if arriba > 0:
                suma_valores += float(arriba) * 1
                suma_pesos += 1
            if abajo > 0:
                suma_valores += float(abajo) * 1
                suma_pesos += 1
            if izquierda > 0:
                suma_valores += float(izquierda) * 1
                suma_pesos += 1
            if derecha > 0:
                suma_valores += float(derecha) * 1
                suma_pesos += 1

            # Vecinos en esquinas (peso 2)
            if esquina_sup_izq > 0:
                suma_valores += float(esquina_sup_izq) * 2
                suma_pesos += 2
            if esquina_sup_der > 0:
                suma_valores += float(esquina_sup_der) * 2
                suma_pesos += 2
            if esquina_inf_izq > 0:
                suma_valores += float(esquina_inf_izq) * 2
                suma_pesos += 2
            if esquina_inf_der > 0:
                suma_valores += float(esquina_inf_der) * 2
                suma_pesos += 2

            if suma_pesos > 0:
                img_filtrada[i, j] = suma_valores / suma_pesos

    return img_filtrada.astype(np.uint8)


# Aplicar ambos métodos
print("\n--- MÉTODO 1: Prioridad Cruz, luego Esquinas ---")
scaled_filtrada = aplicar_filtro_bilineal(scaled_img)

print("\n--- MÉTODO 2: Usar todos los vecinos con pesos ---")
scaled_filtrada_completo = aplicar_filtro_bilineal_completo(scaled_img)

# Mostrar todas las versiones
cv.imshow("1. Original", img)
cv.imshow("2. Escalada (con huecos)", scaled_img)
cv.imshow("3. Filtro: Prioridad Cruz>Esquinas", scaled_filtrada)
cv.imshow("4. Filtro: Todos los vecinos", scaled_filtrada_completo)

print("\n=== COMPARACIÓN ===")
print(f"Píxeles vacíos en escalada: {np.sum(scaled_img == 0)}")
print(
    f"Píxeles vacíos después filtro inteligente: {np.sum(scaled_filtrada == 0)}"
)
print(
    f"Píxeles vacíos después filtro completo: {np.sum(scaled_filtrada_completo == 0)}"
)
print("\nPresiona cualquier tecla para cerrar...")

cv.waitKey(0)
cv.destroyAllWindows()
