import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_robot():
    """Robot LEGO con primitivas OpenGL y detalles de color"""

    # CABEZA CON SOMBRA - GL_QUADS
    glBegin(GL_QUADS)
    # Sombra
    glColor3f(0.8, 0.6, 0.0)
    glVertex2f(-0.15, 0.42)
    glVertex2f(0.15, 0.42)
    glVertex2f(0.15, 0.4)
    glVertex2f(-0.15, 0.4)
    # Cabeza principal
    glColor3f(1.0, 0.8, 0.0)  # Amarillo
    glVertex2f(-0.15, 0.6)
    glVertex2f(0.15, 0.6)
    glVertex2f(0.15, 0.42)
    glVertex2f(-0.15, 0.42)
    glEnd()

    # OJOS - GL_POINTS
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)  # Negro
    glVertex2f(-0.07, 0.53)
    glVertex2f(0.07, 0.53)
    glEnd()

    # PUPILAS - GL_POINTS
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # Blanco
    glVertex2f(-0.065, 0.535)
    glVertex2f(0.075, 0.535)
    glEnd()

    # BOCA - GL_TRIANGLES
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.0)  # Negro
    glVertex2f(-0.06, 0.46)
    glVertex2f(0.06, 0.46)
    glVertex2f(0.0, 0.44)
    glEnd()

    # CUELLO - GL_QUAD_STRIP
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.9, 0.7, 0.0)
    glVertex2f(-0.08, 0.4)
    glVertex2f(-0.08, 0.35)
    glVertex2f(0.08, 0.4)
    glVertex2f(0.08, 0.35)
    glEnd()

    # CUERPO CON DETALLES - GL_QUADS
    glBegin(GL_QUADS)
    # Cuerpo principal
    glColor3f(0.0, 0.5, 1.0)  # Azul
    glVertex2f(-0.22, 0.35)
    glVertex2f(0.22, 0.35)
    glVertex2f(0.22, 0.0)
    glVertex2f(-0.22, 0.0)

    # Panel central más oscuro
    glColor3f(0.0, 0.4, 0.8)
    glVertex2f(-0.12, 0.3)
    glVertex2f(0.12, 0.3)
    glVertex2f(0.12, 0.05)
    glVertex2f(-0.12, 0.05)
    glEnd()

    # BOTONES EN EL PECHO - GL_TRIANGLES
    glBegin(GL_TRIANGLES)
    # Botón superior rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.05, 0.26)
    glVertex2f(0.05, 0.26)
    glVertex2f(0.0, 0.22)
    # Botón medio amarillo
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(-0.05, 0.19)
    glVertex2f(0.05, 0.19)
    glVertex2f(0.0, 0.15)
    # Botón inferior verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.05, 0.12)
    glVertex2f(0.05, 0.12)
    glVertex2f(0.0, 0.08)
    glEnd()

    # HOMBROS - GL_QUADS
    glBegin(GL_QUADS)
    # Hombro izquierdo
    glColor3f(0.0, 0.4, 0.8)
    glVertex2f(-0.25, 0.35)
    glVertex2f(-0.22, 0.35)
    glVertex2f(-0.22, 0.28)
    glVertex2f(-0.25, 0.28)
    # Hombro derecho
    glVertex2f(0.22, 0.35)
    glVertex2f(0.25, 0.35)
    glVertex2f(0.25, 0.28)
    glVertex2f(0.22, 0.28)
    glEnd()

    # BRAZO IZQUIERDO - GL_QUAD_STRIP
    glBegin(GL_QUAD_STRIP)
    glColor3f(1.0, 0.8, 0.0)  # Amarillo
    glVertex2f(-0.25, 0.32)
    glVertex2f(-0.25, 0.25)
    glColor3f(1.0, 0.7, 0.0)
    glVertex2f(-0.32, 0.28)
    glVertex2f(-0.32, 0.21)
    glColor3f(1.0, 0.6, 0.0)
    glVertex2f(-0.36, 0.18)
    glVertex2f(-0.36, 0.11)
    glColor3f(1.0, 0.8, 0.0)
    glVertex2f(-0.38, 0.08)
    glVertex2f(-0.38, 0.01)
    glEnd()

    # MANO IZQUIERDA - GL_QUADS
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.8, 0.0)
    glVertex2f(-0.42, 0.02)
    glVertex2f(-0.34, 0.02)
    glVertex2f(-0.34, -0.05)
    glVertex2f(-0.42, -0.05)
    glEnd()

    # BRAZO DERECHO - GL_QUAD_STRIP
    glBegin(GL_QUAD_STRIP)
    glColor3f(1.0, 0.8, 0.0)  # Amarillo
    glVertex2f(0.25, 0.32)
    glVertex2f(0.25, 0.25)
    glColor3f(1.0, 0.7, 0.0)
    glVertex2f(0.32, 0.28)
    glVertex2f(0.32, 0.21)
    glColor3f(1.0, 0.6, 0.0)
    glVertex2f(0.36, 0.18)
    glVertex2f(0.36, 0.11)
    glColor3f(1.0, 0.8, 0.0)
    glVertex2f(0.38, 0.08)
    glVertex2f(0.38, 0.01)
    glEnd()

    # MANO DERECHA - GL_QUADS
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.8, 0.0)
    glVertex2f(0.34, 0.02)
    glVertex2f(0.42, 0.02)
    glVertex2f(0.42, -0.05)
    glVertex2f(0.34, -0.05)
    glEnd()

    # CINTURA - GL_QUAD_STRIP
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.2, 0.2, 0.2)  # Gris oscuro
    glVertex2f(-0.22, 0.0)
    glVertex2f(-0.22, -0.03)
    glVertex2f(0.22, 0.0)
    glVertex2f(0.22, -0.03)
    glEnd()

    # PIERNA IZQUIERDA - GL_QUAD_STRIP
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.0, 0.5, 1.0)  # Azul
    glVertex2f(-0.16, -0.03)
    glVertex2f(-0.16, -0.12)
    glVertex2f(-0.06, -0.03)
    glVertex2f(-0.06, -0.12)
    # Rodilla
    glColor3f(0.0, 0.4, 0.8)
    glVertex2f(-0.06, -0.18)
    glVertex2f(-0.16, -0.18)
    # Parte inferior
    glColor3f(0.0, 0.5, 1.0)
    glVertex2f(-0.06, -0.3)
    glVertex2f(-0.16, -0.3)
    glEnd()

    # PIERNA DERECHA - GL_QUAD_STRIP
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.0, 0.5, 1.0)  # Azul
    glVertex2f(0.06, -0.03)
    glVertex2f(0.06, -0.12)
    glVertex2f(0.16, -0.03)
    glVertex2f(0.16, -0.12)
    # Rodilla
    glColor3f(0.0, 0.4, 0.8)
    glVertex2f(0.16, -0.18)
    glVertex2f(0.06, -0.18)
    # Parte inferior
    glColor3f(0.0, 0.5, 1.0)
    glVertex2f(0.16, -0.3)
    glVertex2f(0.06, -0.3)
    glEnd()

    # PIES - GL_QUADS
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)  # Gris oscuro
    # Pie izquierdo
    glVertex2f(-0.2, -0.3)
    glVertex2f(-0.02, -0.3)
    glVertex2f(-0.02, -0.4)
    glVertex2f(-0.2, -0.4)
    # Suela izquierda
    glColor3f(0.1, 0.1, 0.1)  # Negro
    glVertex2f(-0.2, -0.4)
    glVertex2f(-0.02, -0.4)
    glVertex2f(-0.02, -0.42)
    glVertex2f(-0.2, -0.42)

    # Pie derecho
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(0.02, -0.3)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.02, -0.4)
    # Suela derecha
    glColor3f(0.1, 0.1, 0.1)
    glVertex2f(0.02, -0.4)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.2, -0.42)
    glVertex2f(0.02, -0.42)
    glEnd()


def main():
    # Inicializa GLFW
    if not glfw.init():
        return

    # Crear ventana (ajustamos el tamaño para que sea más cuadrada y se vea mejor centrado)
    window = glfw.create_window(600, 800, "Robot LEGO", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glClearColor(0.15, 0.15, 0.2, 1.0)  # Fondo azul oscuro

    # Configurar la proyección una vez (no cambia durante el programa)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

    # Bucle principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        # Obtener el tamaño actual de la ventana
        width, height = glfw.get_window_size(window)

        # Configurar viewport para toda la ventana (robot centrado)
        glViewport(0, 0, width, height)

        # Resetear la matriz de modelo/vista
        glLoadIdentity()

        # Dibujar solo el robot detallado
        draw_robot()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
