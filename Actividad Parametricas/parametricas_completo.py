import cv2
import numpy as np

# Configuración de la ventana
width, height = 1000, 1000
center_x, center_y = width // 2, height // 2

# Parámetros globales
theta_increment = 0.05
max_theta = 4 * np.pi  # Dos ciclos completos para algunas curvas
theta = 0
curva_actual = 0

# Diccionario de curvas paramétricas
curvas = {
    0: {"nombre": "Limaçon", "descripcion": "r = a + b*cos(k*t)", "color": (0, 0, 255)},
    1: {
        "nombre": "Cardioide",
        "descripcion": "r = a*(1 + cos(t))",
        "color": (255, 0, 0),
    },
    2: {
        "nombre": "Rosa de 5 petalos",
        "descripcion": "r = a*cos(5*t)",
        "color": (255, 0, 255),
    },
    3: {
        "nombre": "Espiral de Arquimedes",
        "descripcion": "r = a*t",
        "color": (0, 255, 255),
    },
    4: {
        "nombre": "Lemniscata de Bernoulli",
        "descripcion": "r² = a²*cos(2*t)",
        "color": (128, 0, 128),
    },
    5: {
        "nombre": "Cicloide",
        "descripcion": "x=a*(t-sin(t)), y=a*(1-cos(t))",
        "color": (0, 165, 255),
    },
    6: {
        "nombre": "Epicicloide",
        "descripcion": "Circulo rodando sobre circulo",
        "color": (255, 128, 0),
    },
    7: {
        "nombre": "Hipocicloide",
        "descripcion": "Circulo rodando dentro de circulo",
        "color": (0, 255, 128),
    },
    8: {
        "nombre": "Espiral Logaritmica",
        "descripcion": "r = a*e^(b*t)",
        "color": (128, 128, 255),
    },
    9: {
        "nombre": "Curva de Lissajous",
        "descripcion": "x=a*sin(n*t), y=b*sin(m*t)",
        "color": (255, 255, 0),
    },
}


def calcular_punto(t, curva_idx):
    """Calcula las coordenadas (x, y) según la curva seleccionada"""

    if curva_idx == 0:  # Limaçon
        a, b, k = 150, 100, 0.7
        r = a + b * np.cos(k * t)
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))

    elif curva_idx == 1:  # Cardioide
        a = 150
        r = a * (1 + np.cos(t))
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))

    elif curva_idx == 2:  # Rosa de 5 pétalos
        a = 200
        r = a * np.cos(5 * t)
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))

    elif curva_idx == 3:  # Espiral de Arquímedes
        a = 20
        r = a * t
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))

    elif curva_idx == 4:  # Lemniscata de Bernoulli
        a = 150
        # r² = a²*cos(2*t), necesitamos verificar que cos(2*t) >= 0
        cos_val = np.cos(2 * t)
        if cos_val >= 0:
            r = a * np.sqrt(cos_val)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
        else:
            return None  # No dibujar cuando cos(2*t) < 0

    elif curva_idx == 5:  # Cicloide
        a = 80
        x = int(center_x + a * (t - np.sin(t)) - 400)  # Centrar mejor
        y = int(center_y - a * (1 - np.cos(t)) + 200)

    elif curva_idx == 6:  # Epicicloide
        R, r, d = 100, 40, 40  # Radio grande, radio pequeño, distancia
        x = int(center_x + (R + r) * np.cos(t) - d * np.cos((R + r) * t / r))
        y = int(center_y + (R + r) * np.sin(t) - d * np.sin((R + r) * t / r))

    elif curva_idx == 7:  # Hipocicloide
        R, r, d = 150, 50, 50
        x = int(center_x + (R - r) * np.cos(t) + d * np.cos((R - r) * t / r))
        y = int(center_y + (R - r) * np.sin(t) - d * np.sin((R - r) * t / r))

    elif curva_idx == 8:  # Espiral Logarítmica
        a, b = 1, 0.2
        r = a * np.exp(b * t)
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))

    elif curva_idx == 9:  # Curva de Lissajous
        a, b = 200, 200
        n, m = 3, 4  # Frecuencias
        x = int(center_x + a * np.sin(n * t))
        y = int(center_y + b * np.sin(m * t))

    return (x, y)


def dibujar_interfaz(img, curva_idx, theta_actual):
    """Dibuja la información de la curva actual"""
    info = curvas[curva_idx]

    # Fondo semi-transparente para el texto
    overlay = img.copy()
    cv2.rectangle(overlay, (10, 10), (500, 150), (50, 50, 50), -1)
    cv2.addWeighted(overlay, 0.7, img, 0.3, 0, img)

    # Información de la curva
    cv2.putText(
        img,
        f"Curva {curva_idx}: {info['nombre']}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )
    cv2.putText(
        img,
        info["descripcion"],
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 200, 200),
        1,
    )
    cv2.putText(
        img,
        f"Angulo: {theta_actual:.2f} rad",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 200, 200),
        1,
    )

    # Instrucciones
    cv2.putText(
        img,
        "Teclas 0-9: Cambiar curva | ESPACIO: Reiniciar | ESC: Salir",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (150, 255, 150),
        1,
    )


# Inicializar imagen
img = np.ones((height, width, 3), dtype=np.uint8) * 255

print("=" * 60)
print("ECUACIONES PARAMÉTRICAS - GUÍA INTERACTIVA")
print("=" * 60)
print("\nControles:")
print("  Teclas 0-9: Seleccionar curva")
print("  ESPACIO: Reiniciar animación")
print("  ESC: Salir\n")
print("Curvas disponibles:")
for idx, info in curvas.items():
    print(f"  {idx}: {info['nombre']} - {info['descripcion']}")
print("=" * 60 + "\n")

while True:
    # Dibujar la curva completa hasta theta
    for t in np.arange(0, theta, theta_increment):
        punto = calcular_punto(t, curva_actual)

        if punto is not None:
            x, y = punto
            # Verificar que el punto esté dentro de los límites
            if 0 <= x < width and 0 <= y < height:
                color = curvas[curva_actual]["color"]
                cv2.circle(img, (x, y), 2, color, -1)

    # Dibujar interfaz
    dibujar_interfaz(img, curva_actual, theta)

    # Mostrar imagen
    cv2.imshow("Ecuaciones Parametricas", img)

    # Incrementar ángulo
    theta += theta_increment

    # Reiniciar si alcanza el máximo
    if theta >= max_theta:
        theta = 0
        img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Capturar teclas
    key = cv2.waitKey(30) & 0xFF

    if key == 27:  # ESC
        break
    elif key == ord(" "):  # ESPACIO - Reiniciar
        theta = 0
        img = np.ones((height, width, 3), dtype=np.uint8) * 255
    elif ord("0") <= key <= ord("9"):  # Cambiar curva
        nueva_curva = key - ord("0")
        if nueva_curva in curvas:
            curva_actual = nueva_curva
            theta = 0
            img = np.ones((height, width, 3), dtype=np.uint8) * 255
            print(f"\nCurva seleccionada: {curvas[curva_actual]['nombre']}")

cv2.destroyAllWindows()
