import cv2
import mediapipe as mp
import numpy as np

# Inicializar MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

# Captura de video
cap = cv2.VideoCapture(0)

# Puntos clave de la boca (contorno exterior de labios)
BOCA_PUNTOS = [13, 14, 78, 308, 317, 82, 87, 178, 402]

# Variables para seguimiento de gestos
gesto_activo = False
frames_abierta = 0
UMBRAL_APERTURA = 20  # Ajustar según pruebas
FRAMES_CONSECUTIVOS = 5  # Número de frames para confirmar gesto


def calcular_apertura_boca(puntos):
    """Calcula la distancia vertical de apertura de boca"""
    # Puntos superior e inferior del centro de la boca
    superior = np.array(puntos[13])  # Labio superior centro
    inferior = np.array(puntos[14])  # Labio inferior centro

    # Puntos laterales para normalización
    izquierda = np.array(puntos[78])
    derecha = np.array(puntos[308])

    # Calcular distancia vertical normalizada
    distancia_vertical = np.linalg.norm(superior - inferior)
    distancia_horizontal = np.linalg.norm(izquierda - derecha)

    if distancia_horizontal > 0:
        return distancia_vertical / distancia_horizontal
    return 0


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            puntos_boca = {}

            # Extraer coordenadas de puntos de la boca
            for idx in BOCA_PUNTOS:
                landmark = face_landmarks.landmark[idx]
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                puntos_boca[idx] = (x, y)

                # Dibujar puntos de la boca
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Calcular apertura de boca
            if len(puntos_boca) >= 9:
                apertura = calcular_apertura_boca(puntos_boca) * 100

                # Detectar gesto de boca abierta
                if apertura > UMBRAL_APERTURA:
                    frames_abierta += 1
                    if frames_abierta >= FRAMES_CONSECUTIVOS and not gesto_activo:
                        gesto_activo = True
                        print("Boca detectada abierta")
                else:
                    frames_abierta = 0
                    gesto_activo = False

                # Mostrar información
                cv2.putText(
                    frame,
                    f"Apertura: {apertura:.1f}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )
                cv2.putText(
                    frame,
                    f"Estado: {'Abierta' if gesto_activo else 'Cerrada'}",
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

    cv2.imshow("Deteccion de Boca", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
