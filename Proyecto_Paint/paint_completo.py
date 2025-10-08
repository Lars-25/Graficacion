import cv2
import numpy as np

camara = cv2.VideoCapture(0)

# Creamos un lienzo vacío
ret, cuadro = camara.read()
lienzo = np.zeros_like(cuadro)

# Rango del color azul en espacio HSV (para el puntero)
u_bajo = np.array([100, 150, 0])
u_alto = np.array([140, 255, 255])
7
punto_anterior = None
umbral_distancia = 50  # para evitar trazos largos falsos

# Paleta de colores (BGR format)
colores = {
    "rojo": (0, 0, 255),
    "azul": (255, 0, 0),
    "morado": (255, 0, 130),
    "amarillo": (0, 255, 255),
    "verde": (0, 255, 0),
    "rosa": (251, 81, 255),
    "naranja": (72, 143, 240),
    "negro": (0, 0, 0),
}

# Posiciones de los rectángulos de la paleta (x, y, ancho, alto)
paleta_rects = {
    "rojo": (10, 10, 70, 60),
    "azul": (90, 10, 70, 60),
    "morado": (170, 10, 70, 60),
    "amarillo": (250, 10, 70, 60),
    "verde": (330, 10, 70, 60),
    "rosa": (410, 10, 70, 60),
    "naranja": (490, 10, 70, 60),
    "negro": (570, 10, 70, 60),
}

# Color actual seleccionado
color_actual = colores["verde"]
nombre_color_actual = "verde"


def dibujar_paleta(frame):
    """Dibuja la paleta de colores en el frame"""
    for nombre, (x, y, w, h) in paleta_rects.items():
        # Dibujar rectángulo con el color
        cv2.rectangle(frame, (x, y), (x + w, y + h), colores[nombre], -1)
        # Borde blanco
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

        # Marcar el color seleccionado con borde más grueso
        if nombre == nombre_color_actual:
            cv2.rectangle(
                frame, (x - 3, y - 3), (x + w + 3, y + h + 3), color_actual, 3
            )

    # Añadir texto indicando el color actual
    cv2.putText(
        frame,
        f"Color: {nombre_color_actual}",
        (10, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )
    cv2.putText(
        frame,
        "Presiona 'c' para limpiar, ESC para salir",
        (10, frame.shape[0] - 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 255),
        1,
    )


def detectar_seleccion_color(punto):
    """Detecta si el punto está sobre algún rectángulo de la paleta"""
    x, y = punto
    for nombre, (rx, ry, rw, rh) in paleta_rects.items():
        if rx <= x <= rx + rw and ry <= y <= ry + rh:
            return nombre
    return None


while True:
    ret, cuadro = camara.read()
    if not ret:
        break

    hsv = cv2.cvtColor(cuadro, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, u_bajo, u_alto)

    # Momentos de la máscara (para calcular el centroide)
    momentos = cv2.moments(mascara)
    if momentos["m00"] > 0:  # hay píxeles del color buscado
        cx = int(momentos["m10"] / momentos["m00"])
        cy = int(momentos["m01"] / momentos["m00"])
        punto_actual = (cx, cy)

        # Verificar si está seleccionando un color de la paleta
        color_seleccionado = detectar_seleccion_color(punto_actual)
        if color_seleccionado:
            color_actual = colores[color_seleccionado]
            nombre_color_actual = color_seleccionado
            # Dibujar círculo grande para indicar selección
            cv2.circle(cuadro, punto_actual, 10, (0, 255, 255), 3)
        else:
            # Dibujar punto en la cámara CON EL COLOR ACTUAL
            cv2.circle(cuadro, punto_actual, 5, color_actual, -1)

            # Agregar un borde blanco para mejor visibilidad
            cv2.circle(cuadro, punto_actual, 7, (255, 255, 255), 1)

            # Dibujar línea en el lienzo si el salto no es muy grande
            if punto_anterior is not None:
                distancia = np.linalg.norm(
                    np.array(punto_actual) - np.array(punto_anterior)
                )
                if distancia < umbral_distancia:
                    cv2.line(lienzo, punto_anterior, punto_actual, color_actual, 5)

        punto_anterior = punto_actual
    else:
        punto_anterior = None

    # Dibujar la paleta de colores
    dibujar_paleta(cuadro)

    combinado = cv2.add(cuadro, lienzo)

    cv2.imshow("Dibujo en vivo", combinado)
    cv2.imshow("Mascara de color", mascara)
    cv2.imshow("Lienzo", lienzo)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:  # ESC para salir
        break
    elif tecla == ord("c"):  # limpiar lienzo
        lienzo = np.zeros_like(cuadro)

camara.release()
cv2.destroyAllWindows()


"""
TODO:
DibujaR primitivas de dibuja

Cuadros, Circulos
grandmarks libreria
Ampliar
"""
