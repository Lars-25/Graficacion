import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def crear_tux_pixel_art():
    """
    Genera una imagen tipo pixel art del pingüino Tux más apegada a la imagen original.
    Cada color se representa con un valor específico en el rango 0-255.
    """

    # Definir el tamaño de la imagen (siguiendo proporciones de la imagen original)
    ancho, alto = 30, 40

    # Crear matriz inicializada con fondo blanco (255) como la imagen original
    tux = np.full((alto, ancho), 255, dtype=np.uint8)

    # Definir colores usando valores de 0-255
    NEGRO = 0        # Para el contorno y cuerpo negro
    BLANCO = 255     # Para el pecho blanco y ojos
    AMARILLO = 200   # Para el pico y pies
    NARANJA = 150    # Para partes más oscuras del pico y pies
    GRIS_CLARO = 220 # Para sombras sutiles

    # CABEZA DEL PINGÜINO - Forma más redondeada y compacta
    # Parte superior de la cabeza (más redonda)
    cabeza_pixels = [
        # Fila por fila definiendo la forma exacta de la cabeza
        (6, [12, 13, 14, 15, 16, 17]),                    # Top de la cabeza
        (7, [11, 12, 13, 14, 15, 16, 17, 18]),           #
        (8, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),   #
        (9, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),  # Parte más ancha
        (10, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), #
        (11, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), #
        (12, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), #
        (13, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), #
        (14, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), #
    ]

    # Dibujar la cabeza
    for y, x_positions in cabeza_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = NEGRO

    # OJOS - Óvalos blancos más grandes y prominentes como en la imagen original
    # Ojo izquierdo (más grande y ovalado)
    ojo_izq_pixels = [
        (10, [11, 12, 13]),
        (11, [11, 12, 13, 14]),
        (12, [11, 12, 13, 14]),
        (13, [11, 12, 13]),
    ]

    # Ojo derecho
    ojo_der_pixels = [
        (10, [16, 17, 18]),
        (11, [15, 16, 17, 18]),
        (12, [15, 16, 17, 18]),
        (13, [16, 17, 18]),
    ]

    # Dibujar ojos blancos
    for y, x_positions in ojo_izq_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = BLANCO

    for y, x_positions in ojo_der_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = BLANCO

    # PICO - Forma más ancha y redondeada como en la imagen original
    pico_pixels = [
        (13, [14, 15]),           # Parte superior del pico
        (14, [13, 14, 15, 16]),   # Parte media (más ancha)
        (15, [13, 14, 15, 16]),   #
        (16, [14, 15]),           # Parte inferior
    ]

    # Dibujar pico amarillo
    for y, x_positions in pico_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = AMARILLO

    # Parte más oscura del pico (línea central)
    tux[15, 14] = NARANJA
    tux[15, 15] = NARANJA

    # CUERPO - Forma más redondeada y proporcionada
    cuerpo_pixels = []

    # Definir el cuerpo fila por fila
    cuerpo_def = [
        (15, [10, 11, 12, 17, 18, 19]),         # Inicio del cuerpo
        (16, [9, 10, 11, 12, 17, 18, 19, 20]),  #
        (17, [8, 9, 10, 11, 18, 19, 20, 21]),   #
        (18, [7, 8, 9, 10, 19, 20, 21, 22]),    # Parte más ancha
        (19, [7, 8, 9, 10, 19, 20, 21, 22]),    #
        (20, [6, 7, 8, 9, 20, 21, 22, 23]),     #
        (21, [6, 7, 8, 9, 20, 21, 22, 23]),     #
        (22, [6, 7, 8, 9, 20, 21, 22, 23]),     #
        (23, [6, 7, 8, 9, 20, 21, 22, 23]),     #
        (24, [6, 7, 8, 9, 20, 21, 22, 23]),     #
        (25, [6, 7, 8, 9, 20, 21, 22, 23]),     #
        (26, [7, 8, 9, 10, 19, 20, 21, 22]),    #
        (27, [7, 8, 9, 10, 19, 20, 21, 22]),    #
        (28, [8, 9, 10, 11, 18, 19, 20, 21]),   #
        (29, [9, 10, 11, 12, 17, 18, 19, 20]),  #
        (30, [10, 11, 12, 13, 16, 17, 18, 19]), # Parte inferior
    ]

    # Dibujar contorno del cuerpo
    for y, x_positions in cuerpo_def:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = NEGRO

    # PECHO BLANCO - Área interna del cuerpo
    pecho_pixels = [
        (17, [11, 12, 13, 14, 15, 16, 17]),
        (18, [11, 12, 13, 14, 15, 16, 17, 18]),
        (19, [11, 12, 13, 14, 15, 16, 17, 18]),
        (20, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        (21, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        (22, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        (23, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        (24, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        (25, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        (26, [11, 12, 13, 14, 15, 16, 17, 18]),
        (27, [11, 12, 13, 14, 15, 16, 17, 18]),
        (28, [12, 13, 14, 15, 16, 17]),
        (29, [13, 14, 15, 16]),
    ]

    # Dibujar pecho blanco
    for y, x_positions in pecho_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = BLANCO

    # PIES - Formas amarillas más grandes y redondeadas
    # Pie izquierdo
    pie_izq_pixels = [
        (31, [8, 9, 10, 11, 12]),
        (32, [7, 8, 9, 10, 11, 12, 13]),
        (33, [7, 8, 9, 10, 11, 12, 13]),
        (34, [8, 9, 10, 11, 12]),
        (35, [9, 10, 11]),
    ]

    # Pie derecho
    pie_der_pixels = [
        (31, [17, 18, 19, 20, 21]),
        (32, [16, 17, 18, 19, 20, 21, 22]),
        (33, [16, 17, 18, 19, 20, 21, 22]),
        (34, [17, 18, 19, 20, 21]),
        (35, [18, 19, 20]),
    ]

    # Dibujar pies amarillos
    for y, x_positions in pie_izq_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = AMARILLO

    for y, x_positions in pie_der_pixels:
        for x in x_positions:
            if 0 <= y < alto and 0 <= x < ancho:
                tux[y, x] = AMARILLO

    # Detalles en los pies (líneas más oscuras)
    # Pie izquierdo
    for x in [9, 10, 11]:
        tux[33, x] = NARANJA

    # Pie derecho
    for x in [18, 19, 20]:
        tux[33, x] = NARANJA

    # Agregar algunos highlights en los ojos para que se vean más vivos
    tux[11, 12] = GRIS_CLARO  # Brillo en ojo izquierdo
    tux[11, 17] = GRIS_CLARO  # Brillo en ojo derecho

    return tux

def mostrar_tux(imagen):
    """
    Muestra la imagen del pingüino Tux usando OpenCV y matplotlib
    """
    # Crear una versión escalada para visualización (manteniendo pixeles nítidos)
    factor_escala = 12
    alto, ancho = imagen.shape
    tux_escalado = cv.resize(imagen, (ancho * factor_escala, alto * factor_escala),
                            interpolation=cv.INTER_NEAREST)

    # Mostrar con OpenCV
    cv.imshow('Tux - Pixel Art Fiel al Original', tux_escalado)

    # También mostrar con matplotlib
    plt.figure(figsize=(10, 12))
    plt.imshow(imagen, cmap='gray', interpolation='nearest')
    plt.title('Pingüino Tux - Pixel Art\n(Basado en la imagen original)', fontsize=16, fontweight='bold')
    plt.axis('off')

    # Añadir grid para mostrar los píxeles individuales
    plt.grid(True, linewidth=0.5, alpha=0.3)

    # Información sobre la imagen
    plt.figtext(0.02, 0.02,
                f'Dimensiones: {imagen.shape[1]} x {imagen.shape[0]} píxeles\n'
                f'Valores únicos: {len(np.unique(imagen))} colores\n'
                f'Rango: {imagen.min()}-{imagen.max()}\n'
                f'Tipo: {imagen.dtype}',
                fontsize=11, bbox=dict(boxstyle="round,pad=0.4", facecolor="lightblue", alpha=0.8))

    plt.tight_layout()
    plt.show()

    return tux_escalado

def analizar_imagen(imagen):
    """
    Analiza la imagen generada y muestra estadísticas detalladas
    """
    print("="*60)
    print("ANÁLISIS DEL PIXEL ART - PINGÜINO TUX")
    print("="*60)
    print(f"📏 Dimensiones: {imagen.shape[1]} x {imagen.shape[0]} píxeles")
    print(f"💾 Tamaño en memoria: {imagen.nbytes} bytes")
    print(f"🎨 Tipo de datos: {imagen.dtype}")
    print(f"📊 Total de píxeles: {imagen.size}")

    # Análisis de colores
    valores_unicos, conteos = np.unique(imagen, return_counts=True)
    print(f"🌈 Colores únicos: {len(valores_unicos)}")

    # Mapeo de colores a nombres
    mapa_colores = {
        0: "Negro (Contorno/Cuerpo)",
        150: "Naranja (Detalles)",
        200: "Amarillo (Pico/Pies)",
        220: "Gris claro (Highlights)",
        255: "Blanco (Ojos/Pecho/Fondo)"
    }

    print("\n🎨 DISTRIBUCIÓN DE COLORES:")
    print("-" * 40)
    for valor, conteo in zip(valores_unicos, conteos):
        nombre = mapa_colores.get(valor, f"Color-{valor}")
        porcentaje = (conteo / imagen.size) * 100
        barra = "█" * int(porcentaje // 2)  # Barra visual
        print(f"{nombre:25} | {valor:3d} | {conteo:4d} px | {porcentaje:5.1f}% {barra}")

    print("\n✅ Imagen generada exitosamente como matriz de enteros 0-255")

def guardar_imagen(imagen, nombre_archivo='tux_pixel_art_original.png', escala=15):
    """
    Guarda la imagen en alta resolución manteniendo el efecto pixel art
    """
    alto, ancho = imagen.shape
    imagen_hd = cv.resize(imagen, (ancho * escala, alto * escala),
                         interpolation=cv.INTER_NEAREST)

    success = cv.imwrite(nombre_archivo, imagen_hd)
    if success:
        print(f"💾 Imagen guardada: '{nombre_archivo}' ({ancho * escala}x{alto * escala} px)")
    else:
        print("❌ Error al guardar la imagen")

def main():
    """
    Función principal para generar el pixel art fiel al original
    """
    print("🐧 Generando pixel art del pingüino Tux (fiel a la imagen original)...")
    print()

    # Generar la imagen
    tux_imagen = crear_tux_pixel_art()

    # Analizar la imagen
    analizar_imagen(tux_imagen)

    # Guardar la imagen
    guardar_imagen(tux_imagen)

    # Mostrar la imagen
    print("\n🖼️  Mostrando imagen...")
    tux_escalado = mostrar_tux(tux_imagen)

    print("\n⌨️  Presiona cualquier tecla en la ventana de OpenCV para cerrar...")
    cv.waitKey(0)
    cv.destroyAllWindows()

    print("🎉 ¡Pixel art de Tux completado exitosamente!")
    print("📋 Esta imagen cumple con la Actividad 1: Pixel art usando matriz de enteros 0-255")

if __name__ == "__main__":
    main()
