# Apuntes Graficación

## Índice

1. [Manual de Instalación de Git](#manual-de-instalación-de-git)
2. [Manual de Instalación de Python en Windows](#manual-de-instalación-de-python-en-windows)
3. [Entornos Virtuales en Python](#entornos-virtuales-en-python)
4. [Introducción a la Graficación por Computadora](#introducción-a-la-graficación-por-computadora)
5. [Modelos de Color](#modelos-de-color-rgb-cmy-hsv-y-hsl)
6. [Operadores Puntuales](#operadores-puntuales)
7. [Transformaciones Geométricas](#transformaciones-geométricas-en-imágenes)
8. [Landmarks y MediaPipe](#landmarks)
9. [OpenGL](#introducción-a-opengl)
10. [Programación - Ejemplos](#programación)

## Manual de Instalación de Git

### Instalación en Windows
- Descargar desde [https://git-scm.com/](https://git-scm.com/)
- Ejecutar el archivo .exe descargado
- Verificar instalación: `git --version`

### Configuración básica
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@ejemplo.com"
git config --list
```

### Configurar Llave SSH con GitHub
1. **Generar llave SSH**:
   ```bash
   ssh-keygen -t ed25519 -C "tuemail@ejemplo.com"
   ```
2. **Añadir al agente SSH**:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```
3. **Copiar llave pública**:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
4. **Probar conexión**:
   ```bash
   ssh -T git@github.com
   ```

## Manual de Instalación de Python en Windows

### Pasos de Instalación
1. Visitar [https://www.python.org](https://www.python.org)
2. Descargar la versión más reciente
3. **Importante**: Marcar "Add Python to PATH"
4. Verificar instalación: `python --version`

### Verificar pip
```bash
pip --version
```

## Entornos Virtuales en Python

### ¿Qué es un Entorno Virtual?
Un espacio aislado para instalar dependencias específicas de un proyecto, evitando conflictos entre paquetes.

### Crear y Activar Entorno Virtual
```bash
# Crear entorno virtual
python -m venv nombre_entorno

# Activar (Windows)
.\nombre_entorno\Scripts\activate

# Activar (Linux/macOS)
source nombre_entorno/bin/activate

# Desactivar
deactivate
```

### Problema común en PowerShell
Si PowerShell bloquea la ejecución de scripts:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Gestión de Paquetes
```bash
# Instalar paquetes
pip install nombre_paquete

# Generar requirements.txt
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

## Introducción a la Graficación por Computadora

### Definición
La Graficación por Computadora se enfoca en el estudio y aplicación de técnicas, algoritmos y herramientas para la generación y manipulación de imágenes digitales mediante computadoras.

### Objetivos Principales
- **Generación de imágenes**: Crear imágenes 2D y 3D
- **Modelado de objetos**: Representaciones matemáticas usando polígonos y curvas
- **Renderizado**: Convertir representaciones matemáticas en imágenes visuales
- **Transformaciones geométricas**: Traslaciones, rotaciones, escalados y proyecciones
- **Iluminación y sombreado**: Simular interacción de luz con objetos
- **Animación**: Generar secuencias de imágenes que cambian en el tiempo

### ¿Qué es una imagen? (definición formal)
Una imagen digital es una función discreta bidimensional:
```
I : D ⊂ Z² → R^k
```
donde:
- D = {0,...,M-1} × {0,...,N-1} es la malla de píxeles
- k es el número de canales:
  - Escala de grises: k=1
  - Color RGB: k=3

### Transformaciones de Intensidad (píxel a píxel)

#### Brillo
```
I'(x,y) = I(x,y) + β
```

#### Contraste lineal
```
I'(x,y) = α·I(x,y) + β
```

#### Clampeo (saturación)
```
I''(x,y) = min(max(I'(x,y), 0), L-1)
```

## Modelos de Color: RGB, CMY, HSV y HSL

### Modelo RGB (Red, Green, Blue)
- **Modelo aditivo**: Combina luz roja, verde y azul
- **Espacio**: Cubo tridimensional [0,255] para cada canal
- **Conversión a escala de grises**:
  ```
  Y ≈ 0.2126·R + 0.7152·G + 0.0722·B
  ```

### Modelo CMY (Cyan, Magenta, Yellow)
- **Modelo sustractivo**: Para impresión
- **Conversión desde RGB**:
  ```
  C = 1 - R/255
  M = 1 - G/255  
  Y = 1 - B/255
  ```

### Modelo HSV (Hue, Saturation, Value)
- **H (Matiz)**: Ángulo en círculo cromático [0°, 360°)
- **S (Saturación)**: Pureza del color [0,1]
- **V (Valor)**: Brillo del color [0,1]

#### Conversión RGB a HSV
```python
# Normalizar RGB
R' = R/255, G' = G/255, B' = B/255

# Calcular máximo y mínimo
C_max = max(R', G', B')
C_min = min(R', G', B')
Δ = C_max - C_min

# Calcular H
if Δ = 0: H = 0
elif C_max = R': H = 60° × ((G'-B')/Δ mod 6)
elif C_max = G': H = 60° × ((B'-R')/Δ + 2)
elif C_max = B': H = 60° × ((R'-G')/Δ + 4)

# Calcular S
if C_max = 0: S = 0
else: S = Δ/C_max

# Calcular V
V = C_max
```

### HSV en OpenCV
```python
import cv2
import numpy as np

# Definir rango para color verde
lower_green = np.array([35, 100, 100])  # H, S, V mínimos
upper_green = np.array([85, 255, 255])  # H, S, V máximos

# Crear máscara
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_green, upper_green)
```

## Operadores Puntuales

### Definición
Transformaciones aplicadas a cada píxel de manera independiente, donde el valor de salida depende únicamente del valor de entrada de ese píxel.

### Tipos Principales

#### 1. Negativo de Imagen
```
g(x,y) = L - 1 - f(x,y)
```

#### 2. Umbralización (Thresholding)
```python
if f(x,y) ≤ T:
    g(x,y) = 0
else:
    g(x,y) = L
```

#### 3. Corrección Gamma
```
g(x,y) = c · f(x,y)^γ
```

#### 4. Transformación Logarítmica
```
g(x,y) = c · log(1 + f(x,y))
```

### Ejemplo en Python
```python
import cv2 as cv

img = cv.imread('imagen.png', 0)
x, y = img.shape

# Umbralización manual
for i in range(x):
    for j in range(y):
        if img[i,j] > 150:
            img[i,j] = 255
        else:
            img[i,j] = 0
```

## Transformaciones Geométricas en Imágenes

### Coordenadas Homogéneas
```
[x']   [a11  a12  tx]   [x]
[y'] = [a21  a22  ty] × [y]
[1 ]   [0    0    1 ]   [1]
```

### 1. Traslación
```python
# Matriz de traslación
T = [[1, 0, tx],
     [0, 1, ty],
     [0, 0, 1]]

# Fórmula
x' = x + tx
y' = y + ty
```

### 2. Rotación
```python
import math

# Matriz de rotación
theta = math.radians(angle)
R = [[cos(theta), -sin(theta), 0],
     [sin(theta),  cos(theta), 0],
     [0,           0,          1]]

# Fórmulas
x' = x·cos(θ) - y·sin(θ)
y' = x·sin(θ) + y·cos(θ)
```

### 3. Escalado
```python
# Matriz de escalado
S = [[sx, 0,  0],
     [0,  sy, 0],
     [0,  0,  1]]

# Fórmulas
x' = sx · x
y' = sy · y
```

### 4. Cizallamiento (Shearing)
```python
# Horizontal
Shx = [[1,  hx, 0],
       [0,  1,  0],
       [0,  0,  1]]

# Vertical
Shy = [[1,  0,  0],
       [hy, 1,  0],
       [0,  0,  1]]
```

## Operaciones Bitwise en OpenCV

### Funciones Principales
```python
import cv2
import numpy as np

# AND - Intersección
result = cv2.bitwise_and(img1, img2)

# OR - Unión
result = cv2.bitwise_or(img1, img2)

# XOR - Diferencia exclusiva
result = cv2.bitwise_xor(img1, img2)

# NOT - Inversión
result = cv2.bitwise_not(img)
```

### Ejemplo: Máscara
```python
# Crear máscara binaria
ret, mask = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Aplicar máscara
img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img_fg = cv2.bitwise_and(logo, logo, mask=mask)
result = cv2.add(img_bg, img_fg)
```

## Landmarks

### Definición
Puntos clave dentro de una imagen que describen características importantes de un objeto.

### Aplicaciones
- **Reconocimiento facial**: 68 puntos faciales
- **Detección de manos**: 21 puntos de referencia
- **Análisis de postura**: Puntos del cuerpo humano
- **Imágenes médicas**: Estructuras anatómicas

### MediaPipe - Detección de Manos
```python
import cv2
import mediapipe as mp

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar manos
    results = hands.process(frame_rgb)
    
    # Dibujar landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, 
                                    mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("Detección de Manos", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Índice de Dedos en MediaPipe
| Índice | Punto | Descripción |
|--------|-------|-------------|
| 0 | Muñeca | Base de la mano |
| 4 | Punta del pulgar | Extremo del pulgar |
| 8 | Punta del índice | Extremo del índice |
| 12 | Punta del medio | Extremo del medio |
| 16 | Punta del anular | Extremo del anular |
| 20 | Punta del meñique | Extremo del meñique |

## Introducción a OpenGL

### Características de OpenGL
- API estándar para gráficos 2D y 3D
- Multiplataforma
- Pipeline gráfico programable
- Soporte para shaders

### Sistema de Coordenadas
- **Coordenadas del mundo**: Sistema 3D global
- **Coordenadas de vista**: Relativas a la cámara
- **Coordenadas de pantalla**: Píxeles en ventana

### Primitivas de Dibujo
- **GL_POINTS**: Puntos individuales
- **GL_LINES**: Líneas
- **GL_TRIANGLES**: Triángulos
- **GL_QUADS**: Cuadriláteros

### Transformaciones
```c
// Traslación
glTranslatef(x, y, z);

// Rotación
glRotatef(angle, x, y, z);

// Escalado
glScalef(sx, sy, sz);
```

### Proyección Perspectiva
```c
gluPerspective(fovy, aspect, zNear, zFar);
```

## Programación

### Cargar y Mostrar Imagen
```python
import cv2 as cv

# Cargar imagen (0=escala de grises, 1=color)
img = cv.imread('imagen.png', 0)

# Mostrar imagen
cv.imshow('ventana', img)
cv.waitKey(0)
cv.destroyAllWindows()
```

### Crear Imagen desde Matriz
```python
import numpy as np
import cv2 as cv

# Crear imagen 500x500 en gris claro
img = np.ones((500, 500), dtype=np.uint8) * 240

# Modificar píxeles específicos
img[30, 30:36] = 1  # Línea negra

cv.imshow('imagen_creada', img)
cv.waitKey()
cv.destroyAllWindows()
```

### Separar Canales de Color
```python
import cv2 as cv
import numpy as np

img = cv.imread('imagen.png', 1)
img2 = np.zeros(img.shape[:2], dtype=np.uint8)

# Separar canales RGB
b, g, r = cv.split(img)

# Crear imágenes de un solo canal
b_img = cv.merge([b, img2, img2])  # Solo azul
g_img = cv.merge([img2, g, img2])  # Solo verde  
r_img = cv.merge([img2, img2, r])  # Solo rojo

# Mostrar resultados
cv.imshow('Original', img)
cv.imshow('Canal Azul', b_img)
cv.imshow('Canal Verde', g_img)
cv.imshow('Canal Rojo', r_img)
```

### Captura de Video
```python
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        # Mostrar video original
        cv.imshow('video', frame)
        
        # Convertir a escala de grises
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('gris', gray)
        
        # Convertir a HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('hsv', hsv)
        
        # Salir con ESC
        if cv.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
```

### Transformación Geométrica - Traslación (Raw)
```python
import cv2 as cv
import numpy as np

img = cv.imread('imagen.png', 0)
x, y = img.shape

# Crear imagen vacía
translated_img = np.zeros((x, y), dtype=np.uint8)

# Parámetros de traslación
dx, dy = 100, 50

# Aplicar traslación
for i in range(x):
    for j in range(y):
        new_x = i + dy
        new_y = j + dx
        if 0 <= new_x < x and 0 <= new_y < y:
            translated_img[new_x, new_y] = img[i, j]

cv.imshow('Original', img)
cv.imshow('Trasladada', translated_img)
cv.waitKey(0)
cv.destroyAllWindows()
```

## Actividades de Práctica

1. **Pixel Art**: Generar imagen tipo pixel art usando matriz de enteros [0-255]
2. **Operadores Puntuales**: Implementar al menos 5 operadores puntuales
3. **Transformaciones Geométricas**: Aplicar todas las transformaciones vistas
4. **Ecuaciones Paramétricas**: Investigar y programar 10 ecuaciones paramétricas
5. **Primitivas de Dibujo**: Crear dibujos usando OpenCV
6. **Documentación**: Todo en formato Markdown en repositorio

## Conceptos Avanzados

### Filtrado Espacial (Convolución)
```
(I * h)(x,y) = Σ Σ I(x-u,y-v)·h(u,v)
```

#### Kernels Comunes
- **Media (Blur) 3×3**:
  ```
  h = 1/9 * [1 1 1]
            [1 1 1]
            [1 1 1]
  ```

- **Sobel (Gradiente)**:
  ```
  Sx = [-1 0 1]    Sy = [-1 -2 -1]
       [-2 0 2]         [ 0  0  0]
       [-1 0 1]         [ 1  2  1]
  ```

### Transformada Discreta de Fourier 2D
```
F(u,v) = Σ Σ I(x,y)·e^(-j2π(ux/M + vy/N))
```

### Modelo de Cámara Pinhole
```
λ[x]     [fx  0 cx][R|t][X]
 [y]  =  [ 0 fy cy]     [Y]
 [1]     [ 0  0  1]     [Z]
                        [1]
```
