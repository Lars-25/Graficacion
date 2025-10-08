import cv2 as cv

face = cv.CascadeClassifier("cascade/haarcascade_frontalface_alt2.xml")
cap = cv.VideoCapture(0)

# Variables para animación de boca
mouth_size = 0.0
prev_mouth_value = 0

while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gris, 1.3, 5)

    for x, y, w, h in faces:
        # Calcular factor de escala basado en el tamaño del rostro
        scale_factor = (w + h) / 2 / 150
        scale_factor = max(0.5, min(scale_factor, 2.0))

        # Dibujar detalles en el rostro detectado con escala
        res = int((w + h) / 8)

        # Extraer región de la boca (tercio inferior del rostro)
        mouth_region_y = y + int(h * 0.65)
        mouth_region_h = int(h * 0.3)
        mouth_region_x = x + int(w * 0.3)
        mouth_region_w = int(w * 0.4)

        # Asegurar que la región está dentro de los límites
        if (
            mouth_region_y + mouth_region_h < gris.shape[0]
            and mouth_region_x + mouth_region_w < gris.shape[1]
        ):
            mouth_roi = gris[
                mouth_region_y : mouth_region_y + mouth_region_h,
                mouth_region_x : mouth_region_x + mouth_region_w,
            ]

            # Aplicar umbral para detectar áreas oscuras (boca abierta)
            _, thresh = cv.threshold(mouth_roi, 50, 255, cv.THRESH_BINARY_INV)

            # Contar píxeles oscuros (posible apertura de boca)
            dark_pixels = cv.countNonZero(thresh)
            total_pixels = mouth_roi.shape[0] * mouth_roi.shape[1]
            dark_ratio = dark_pixels / total_pixels if total_pixels > 0 else 0

            # Si hay suficientes píxeles oscuros, la boca está abierta
            if dark_ratio > 0.25:  # Umbral ajustable
                mouth_size = min(mouth_size + 0.2, 1.0)
            else:
                mouth_size = max(mouth_size - 0.2, 0.0)

        # Dibujar un rectángulo alrededor del rostro
        img = cv.rectangle(
            img, (x, y), (x + w, y + h), (234, 23, 23), max(2, int(5 * scale_factor))
        )
        img = cv.rectangle(
            img,
            (x, int(y + h / 2)),
            (x + w, y + h),
            (0, 255, 0),
            max(2, int(5 * scale_factor)),
        )

        # Ojos con escala
        eye_radius_outer = max(10, int(19 * scale_factor))
        eye_radius_inner = max(8, int(18 * scale_factor))
        eye_pupil = max(2, int(5 * scale_factor))

        img = cv.circle(
            img,
            (x + int(w * 0.3), y + int(h * 0.4)),
            eye_radius_outer,
            (0, 0, 0),
            max(1, int(2 * scale_factor)),
        )
        img = cv.circle(
            img,
            (x + int(w * 0.7), y + int(h * 0.4)),
            eye_radius_outer,
            (0, 0, 0),
            max(1, int(2 * scale_factor)),
        )
        img = cv.circle(
            img,
            (x + int(w * 0.3), y + int(h * 0.4)),
            eye_radius_inner,
            (255, 255, 255),
            -1,
        )
        img = cv.circle(
            img,
            (x + int(w * 0.7), y + int(h * 0.4)),
            eye_radius_inner,
            (255, 255, 255),
            -1,
        )
        img = cv.circle(
            img, (x + int(w * 0.3), y + int(h * 0.4)), eye_pupil, (0, 0, 255), -1
        )
        img = cv.circle(
            img, (x + int(w * 0.7), y + int(h * 0.4)), eye_pupil, (0, 0, 255), -1
        )

        # Boca animada - se agranda cuando se detecta apertura
        mouth_thickness = max(5, int(10 * scale_factor))

        # Cuando mouth_size es alto, la boca se abre (elipse)
        if mouth_size > 0.3:
            # Boca abierta como elipse
            mouth_radius_x = max(10, int(20 * scale_factor * (1 + mouth_size * 0.5)))
            mouth_radius_y = max(5, int(12 * scale_factor * mouth_size))

            img = cv.ellipse(
                img,
                (x + int(w * 0.5), y + int(h * 0.75)),
                (mouth_radius_x, mouth_radius_y),
                0,
                0,
                180,
                (0, 0, 255),
                mouth_thickness,
            )
        else:
            # Boca cerrada como línea
            img = cv.line(
                img,
                (x + int(w * 0.4), y + int(h * 0.75)),
                (x + int(w * 0.6), y + int(h * 0.75)),
                (0, 0, 255),
                mouth_thickness,
            )

        # Orejas con escala (elipses)
        ear_size = (
            max(5, int(res // 2 * scale_factor / 2)),
            max(10, int(res * scale_factor / 2)),
        )
        img = cv.ellipse(
            img,
            (x + int(w * 0.001), y + int(h * 0.6)),
            ear_size,
            0,
            0,
            360,
            (147, 66, 245),
            max(2, int(5 * scale_factor)),
        )
        img = cv.ellipse(
            img,
            (x + int(w * 1.001), y + int(h * 0.6)),
            ear_size,
            0,
            0,
            360,
            (147, 66, 245),
            max(2, int(5 * scale_factor)),
        )

        # Nariz con escala (círculo)
        nose_radius = max(5, int(res // 5 * scale_factor))
        img = cv.circle(
            img, (x + int(w * 0.5), y + int(h * 0.5)), nose_radius, (0, 255, 255), -1
        )

        # SOMBRERO MEJORADO (solo con rectángulos)
        hat_brim_height = max(15, int(h * 0.15 * scale_factor))
        hat_crown_height = max(40, int(h * 0.4 * scale_factor))
        hat_crown_width = int(w * 0.7)

        # Rectángulo ancho
        img = cv.rectangle(
            img,
            (x - int(w * 0.15), y - hat_brim_height),
            (x + w + int(w * 0.15), y),
            (0, 0, 0),
            -1,
        )

        # Rectángulo alto
        crown_x = x + int(w * 0.15)
        img = cv.rectangle(
            img,
            (crown_x, y - hat_brim_height - hat_crown_height),
            (crown_x + hat_crown_width, y - hat_brim_height),
            (0, 0, 0),
            -1,
        )

        # Banda rectángulo
        band_height = max(8, int(h * 0.08 * scale_factor))
        img = cv.rectangle(
            img,
            (crown_x, y - hat_brim_height - band_height),
            (crown_x + hat_crown_width, y - hat_brim_height),
            (180, 50, 50),
            -1,
        )

    cv.imshow("img", img)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
