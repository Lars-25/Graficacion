
# 📘 Explicación del Código: Capa de Invisibilidad con OpenCV

Este programa en **Python** utiliza **OpenCV** y **NumPy** para crear un efecto de “capa de invisibilidad”, similar a lo visto en películas de fantasía. La idea principal es **detectar un color específico (verde en este caso) y reemplazarlo por el fondo previamente capturado**.

---

## 🔹 Importación de librerías

```python
import cv2
import numpy as np
```

* **cv2**: Librería de OpenCV para visión por computadora (captura de video, procesamiento de imágenes).
* **numpy**: Librería para manejo de arreglos, utilizada aquí para definir rangos de colores.

---

## 🔹 Captura de video desde la cámara

```python
cap = cv2.VideoCapture(0)
cv2.waitKey(2000)
```

* `cv2.VideoCapture(0)` abre la cámara web del dispositivo (índice `0` se refiere a la cámara principal).
* `cv2.waitKey(2000)` espera **2 segundos** para que la cámara se estabilice antes de tomar el fondo.

---

## 🔹 Captura del fondo de referencia

```python
ret, background = cap.read()
if not ret:
    print("Error al capturar el fondo.")
    cap.release()
    exit()
```

* Se toma una **imagen del fondo** (sin la persona ni la tela verde).
* Si la captura falla (`ret == False`), se libera la cámara y se cierra el programa.

---

## 🔹 Bucle principal de procesamiento de video

```python
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
```

* El programa entra en un bucle mientras la cámara esté encendida.
* `frame` es cada cuadro de video capturado.

---

## 🔹 Conversión a espacio de color HSV

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

* Se convierte la imagen de **BGR** (formato por defecto en OpenCV) a **HSV** (Tono, Saturación, Valor).
* HSV facilita la detección de colores específicos (más estable que trabajar con RGB).

---

## 🔹 Definición del rango de color verde

```python
lower_green = np.array([80, 40, 40])
upper_green = np.array([145, 255, 255])
```

* Se define un rango de **verde** en HSV.
* Los valores pueden ajustarse dependiendo de la tela usada y la iluminación.

---

## 🔹 Creación de la máscara del color verde

```python
mask = cv2.inRange(hsv, lower_green, upper_green)
```

* `cv2.inRange()` genera una **máscara binaria**:

  * **Blanco (255):** píxeles dentro del rango verde.
  * **Negro (0):** píxeles fuera del rango.

---

## 🔹 Inversión de la máscara

```python
mask_inv = cv2.bitwise_not(mask)
```

* Se invierte la máscara:

  * **Áreas verdes → Negro**
  * **Áreas no verdes → Blanco**

Esto permitirá aislar las partes de la persona que no son verdes.

---

## 🔹 Extracción de regiones visibles y ocultas

```python
res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
res2 = cv2.bitwise_and(background, background, mask=mask)
```

* **`res1`**: Contiene la persona y los objetos que **no son verdes**.
* **`res2`**: Contiene únicamente las áreas donde **había verde**, pero reemplazadas con el fondo.

---

## 🔹 Combinación de resultados

```python
final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
```

* Se combinan ambas imágenes (`res1` y `res2`) para crear la ilusión de invisibilidad:

  * La persona aparece completa, excepto en las zonas cubiertas con verde, donde se muestra el fondo.

---

## 🔹 Visualización de resultados

```python
cv2.imshow("Capa de Invisibilidad", final_output)
cv2.imshow('mask', mask)
```

* **Ventana 1:** Muestra el efecto final de invisibilidad.
* **Ventana 2:** Muestra la máscara binaria usada para detectar el color verde.

---

## 🔹 Salida del programa

```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
```

* Se espera la tecla **`q`** para salir del bucle.
* Se liberan los recursos (`cap.release()`) y se cierran todas las ventanas (`cv2.destroyAllWindows()`).

