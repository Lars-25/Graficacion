import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
)

cap = cv2.VideoCapture(0)

# Definir la matriz de números y operaciones
numbers = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

operations = ["+", "-", "*", "/"]

# Variables para el estado de la calculadora
current_input = ""
first_number = None
operator = None
result = None
selected_button = None

# Colores
COLOR_BG = (240, 240, 240)
COLOR_BUTTON = (200, 200, 200)
COLOR_HIGHLIGHT = (100, 200, 255)
COLOR_TEXT = (0, 0, 0)
COLOR_RESULT = (0, 100, 0)


def draw_calculator(frame):
    h, w, _ = frame.shape

    # Dibujar fondo de la calculadora
    cv2.rectangle(frame, (0, 0), (w, h), COLOR_BG, -1)

    # Dibujar display
    cv2.rectangle(frame, (20, 20), (w - 20, 80), (255, 255, 255), -1)
    cv2.rectangle(frame, (20, 20), (w - 20, 80), (0, 0, 0), 2)

    # Mostrar contenido del display
    display_text = current_input if result is None else str(result)
    cv2.putText(
        frame, display_text, (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, COLOR_TEXT, 2
    )

    # Dibujar matriz de números
    button_width = (w - 100) // 3
    button_height = 60

    for i in range(3):
        for j in range(3):
            x1 = 20 + j * (button_width + 10)
            y1 = 100 + i * (button_height + 10)
            x2 = x1 + button_width
            y2 = y1 + button_height

            # Resaltar botón seleccionado
            if selected_button == numbers[i][j]:
                cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_HIGHLIGHT, -1)
            else:
                cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_BUTTON, -1)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
            cv2.putText(
                frame,
                numbers[i][j],
                (x1 + button_width // 2 - 10, y1 + button_height // 2 + 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                COLOR_TEXT,
                2,
            )

    # Dibujar operaciones
    op_x = 20 + 3 * (button_width + 10)
    op_width = (w - op_x - 30) // 2
    op_height = 60

    for i, op in enumerate(operations):
        x1 = op_x + (i % 2) * (op_width + 10)
        y1 = 100 + (i // 2) * (op_height + 10)
        x2 = x1 + op_width
        y2 = y1 + op_height

        # Resaltar botón seleccionado
        if selected_button == op:
            cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_HIGHLIGHT, -1)
        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_BUTTON, -1)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
        cv2.putText(
            frame,
            op,
            (x1 + op_width // 2 - 10, y1 + op_height // 2 + 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            COLOR_TEXT,
            2,
        )

    # Botón de igual/calcular
    eq_x = op_x
    eq_y = 100 + 2 * (op_height + 10)
    eq_width = w - eq_x - 20

    if selected_button == "=":
        cv2.rectangle(
            frame,
            (eq_x, eq_y),
            (eq_x + eq_width, eq_y + op_height),
            COLOR_HIGHLIGHT,
            -1,
        )
    else:
        cv2.rectangle(
            frame, (eq_x, eq_y), (eq_x + eq_width, eq_y + op_height), COLOR_BUTTON, -1
        )

    cv2.rectangle(
        frame, (eq_x, eq_y), (eq_x + eq_width, eq_y + op_height), (0, 0, 0), 2
    )
    cv2.putText(
        frame,
        "=",
        (eq_x + eq_width // 2 - 10, eq_y + op_height // 2 + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        COLOR_TEXT,
        2,
    )

    # Botón de limpiar
    clear_x = 20
    clear_y = 100 + 3 * (button_height + 10)
    clear_width = w - 40

    if selected_button == "C":
        cv2.rectangle(
            frame,
            (clear_x, clear_y),
            (clear_x + clear_width, clear_y + op_height),
            (255, 100, 100),
            -1,
        )
    else:
        cv2.rectangle(
            frame,
            (clear_x, clear_y),
            (clear_x + clear_width, clear_y + op_height),
            (200, 100, 100),
            -1,
        )

    cv2.rectangle(
        frame,
        (clear_x, clear_y),
        (clear_x + clear_width, clear_y + op_height),
        (0, 0, 0),
        2,
    )
    cv2.putText(
        frame,
        "Limpiar",
        (clear_x + clear_width // 2 - 40, clear_y + op_height // 2 + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        COLOR_TEXT,
        2,
    )


def is_point_in_rect(point, rect):
    x, y = point
    x1, y1, x2, y2 = rect
    return x1 <= x <= x2 and y1 <= y <= y2


def process_calculator_input(button):
    global current_input, first_number, operator, result

    if button.isdigit():
        current_input += button
    elif button in operations:
        if current_input:
            first_number = float(current_input)
            operator = button
            current_input = ""
    elif button == "=":
        if first_number is not None and operator is not None and current_input:
            second_number = float(current_input)
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                if second_number != 0:
                    result = first_number / second_number
                else:
                    result = "Error"
            current_input = ""
            first_number = None
            operator = None
    elif button == "C":
        current_input = ""
        first_number = None
        operator = None
        result = None


prev_index_pos = None
selection_cooldown = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    # Convertir imagen a RGB (MediaPipe usa RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Dibujar la calculadora
    draw_calculator(frame)

    # Variables para guardar coordenadas del índice
    index_pos = None

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks, results.multi_handedness
        ):
            label = handedness.classification[0].label  # 'Left' o 'Right'
            h, w, _ = frame.shape

            # Coordenadas del índice (landmark 8)
            index_tip = hand_landmarks.landmark[8]
            x, y = int(index_tip.x * w), int(index_tip.y * h)

            # Guardar posición del índice (usaremos solo una mano)
            if index_pos is None:
                index_pos = (x, y)

                # Dibujar un círculo en la punta del índice
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            # Dibujar los landmarks (opcional)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Detectar selección de botones
    selected_button = None

    if index_pos is not None:
        x, y = index_pos

        # Verificar si el dedo está sobre algún botón
        button_width = (frame.shape[1] - 100) // 3
        button_height = 60

        # Verificar números
        for i in range(3):
            for j in range(3):
                x1 = 20 + j * (button_width + 10)
                y1 = 100 + i * (button_height + 10)
                x2 = x1 + button_width
                y2 = y1 + button_height

                if is_point_in_rect((x, y), (x1, y1, x2, y2)):
                    selected_button = numbers[i][j]
                    break

        # Verificar operaciones
        op_x = 20 + 3 * (button_width + 10)
        op_width = (frame.shape[1] - op_x - 30) // 2

        for i, op in enumerate(operations):
            x1 = op_x + (i % 2) * (op_width + 10)
            y1 = 100 + (i // 2) * (button_height + 10)
            x2 = x1 + op_width
            y2 = y1 + button_height

            if is_point_in_rect((x, y), (x1, y1, x2, y2)):
                selected_button = op

        # Verificar botón de igual
        eq_x = op_x
        eq_y = 100 + 2 * (button_height + 10)
        eq_width = frame.shape[1] - eq_x - 20

        if is_point_in_rect(
            (x, y), (eq_x, eq_y, eq_x + eq_width, eq_y + button_height)
        ):
            selected_button = "="

        # Verificar botón de limpiar
        clear_x = 20
        clear_y = 100 + 3 * (button_height + 10)
        clear_width = frame.shape[1] - 40

        if is_point_in_rect(
            (x, y), (clear_x, clear_y, clear_x + clear_width, clear_y + button_height)
        ):
            selected_button = "C"

        # Procesar selección (evitar múltiples activaciones)
        if selected_button and selection_cooldown <= 0:
            process_calculator_input(selected_button)
            selection_cooldown = 20  # Cooldown de 20 frames

    # Actualizar cooldown
    if selection_cooldown > 0:
        selection_cooldown -= 1

    # Actualizar posición anterior
    prev_index_pos = index_pos

    cv2.imshow("Calculadora con Gestos", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
