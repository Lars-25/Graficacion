import sys

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Crear un triangulo 3D que rote segun el angulo en ejes X e Y

# Variables globales
window = None
angle_x, angle_y = 0, 0  # Ángulos de rotación en los ejes X e Y
last_x, last_y = None, None  # Última posición del ratón para calcular


def init():
    # Configuración inicial de OpenGL
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Color de fondo
    glEnable(GL_DEPTH_TEST)  # Activar prueba de profundidad para 3D

    # Configuración de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)

    # Cambiar a la matriz de modelo para los objetos
    glMatrixMode(GL_MODELVIEW)


def draw_triangle():
    global angle_x, angle_y
    glClear(
        GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT
    )  # Limpiar pantalla y buffer de profundidad

    # Configuración de la vista del triángulo
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)  # Alejar el triángulo para que sea visible
    glRotatef(angle_x, 1, 0, 0)  # Rotar el triángulo en el eje X
    glRotatef(angle_y, 0, 1, 0)  # Rotar el triángulo en el eje Y

    # Dibujar la base del triángulo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, 1.0, 0.0)

    # Dibujar las otras dos caras del triángulo para darle volumen
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(0.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, 1.0, 0.0)

    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(0.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, 1.0, 0.0)

    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, -1.0, 1.0)

    glEnd()

    glFlush()
    glfw.swap_buffers(window)  # Intercambiar buffers para animación suave
    angle_x += 0.01  # Incrementar el ángulo para rotación
    angle_y += 0.01  # Incrementar el ángulo para rotación


def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()

    # Crear ventana de GLFW
    width, height = 500, 500
    window = glfw.create_window(
        width, height, "Triangulo 3D Rotando con GLFW", None, None
    )
    if not window:
        glfw.terminate()
        sys.exit()

    # Configurar el contexto de OpenGL en la ventana
    glfw.make_context_current(window)

    # Configuración de viewport y OpenGL
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_triangle()
        glfw.poll_events()

    glfw.terminate()  # Cerrar GLFW al salir


if __name__ == "__main__":
    main()
