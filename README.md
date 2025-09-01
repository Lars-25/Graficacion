# Graficación por Computadora

## Introducción

La **Graficación por Computadora** (o simplemente **Graficación**) se enfoca en el estudio y aplicación de técnicas, algoritmos y herramientas para la generación y manipulación de imágenes digitales mediante el uso de computadoras.  
Es una rama de la informática que combina conceptos de **matemáticas, física y programación** para crear imágenes, animaciones y efectos visuales.

---

## Objetivos principales de la graficación

- **Generación de imágenes** a partir de representaciones en 2D y 3D.  
- **Modelado de objetos** usando polígonos, mallas y curvas.  
- **Renderizado** con iluminación, sombras y texturas.  
- **Transformaciones geométricas**: traslación, rotación, escalado y proyecciones.  
- **Iluminación y sombreado** para simular la interacción de la luz.  
- **Animación**: creación de secuencias dinámicas y simulación física.  
- **Texturizado**: añadir detalles visuales sin aumentar la complejidad geométrica.  
- **Interacción gráfica** en interfaces, realidad virtual y aumentada.  

---

## ¿Qué es una imagen?

Una **imagen digital** puede representarse como una función discreta bidimensional:

`I` : `D` ⊆ `Z²` → `Rᵏ`

donde:

`D` = {0, …, `M-1`} × {0, …, `N-1`} es la cuadrícula de píxeles.

`k` es el número de canales (por ejemplo, `k` = 1 en escala de grises, `k` = 3 en RGB).


### Representación en memoria
- **Escala de grises**: matriz \(M \times N\).  
- **RGB**: tensor \(M \times N \times 3\) o tres matrices separadas (R, G, B).  

---

## Modelos de color

### RGB (Red, Green, Blue)

- Modelo aditivo basado en la combinación de intensidades de los tres colores primarios.  
- Ejemplos de combinaciones:  
  - `(255,0,0)` → rojo  
  - `(0,255,0)` → verde  
  - `(0,0,255)` → azul  
  - `(255,255,0)` → amarillo  
  - `(255,255,255)` → blanco  
  - `(0,0,0)` → negro  

El modelo puede visualizarse como un **cubo tridimensional** de colores.

---

## Librerías principales en Python

A lo largo de la materia se emplean diversas librerías para **procesamiento de datos, visualización y visión por computadora**:

```python
import pandas as pd         # Análisis y manipulación de datos
import numpy as np          # Operaciones matemáticas y algebra lineal
import matplotlib.pyplot as plt  # Visualización en 2D
import seaborn as sns       # Gráficos estadísticos (sobre matplotlib)

# Visión por computadora
import cv2                  # OpenCV: procesamiento y análisis de imágenes
import PIL                  # Pillow: manipulación de imágenes
```
---

## Referencias y Enlaces

- **Sitio web del curso**: [Apuntes Graficación](https://ealcaraz85.github.io/Graficacion.io/)
- **Profesor:** Jesus Eduardo Alcaraz Chavez
- **Alumno:** Luis Arturo Román Sánchez