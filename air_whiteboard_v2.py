import cv2
import numpy as np
import mediapipe as mp
import pytesseract
import sympy as sp

pytesseract.pytesseract.tesseract_cmd = r"D:\New Program Files\tesseract.exe"

print("🚀 AI Whiteboard v2 Started")

# ---------------- Mediapipe ----------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ---------------- Camera ----------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

canvas = None
prev_x, prev_y = 0, 0

# ---------------- OCR FUNCTION ----------------
def recognize(canvas_img):
    gray = cv2.cvtColor(canvas_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    text = pytesseract.image_to_string(thresh)
    return text.strip()

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    if canvas is None:
        canvas = np.zeros((h, w), dtype=np.uint8)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        x = int(lm[8].x * w)
        y = int(lm[8].y * h)

        index_up = lm[8].y < lm[6].y
        middle_up = lm[12].y < lm[10].y
        thumb_up = lm[4].y < lm[3].y

        # ✊ CLEAR
        if not index_up and not middle_up:
            canvas = np.zeros((h, w), dtype=np.uint8)
            prev_x, prev_y = 0, 0
            cv2.putText(frame, "CLEARED", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        # ✍️ DRAW
        elif index_up and not middle_up:

            if prev_x == 0:
                prev_x, prev_y = x, y

            cv2.line(canvas, (prev_x, prev_y), (x, y), 255, 8)
            prev_x, prev_y = x, y

        # ✌️ SPACE (gesture)
        elif index_up and middle_up:
            prev_x, prev_y = 0, 0

        # 👍 NEW LINE (thumb up)
        elif thumb_up:
            prev_x, prev_y = 0, 0
            cv2.putText(frame, "NEW LINE", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        else:
            prev_x, prev_y = 0, 0

        cv2.circle(frame, (x, y), 8, (0,255,0), -1)

    # ---------------- Overlay ----------------
    output = cv2.add(frame, cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR))

    cv2.imshow("AI Whiteboard v2", output)

    key = cv2.waitKey(1)

    # 🧠 OCR + Solve
    if key == ord('r'):
        cv2.imwrite("drawing.png", canvas)
        img = cv2.imread("drawing.png")

        text = recognize(img)
        print("\n🧠 Recognized:", text)

        try:
            result = sp.sympify(text)
            print("➗ Result:", result)
        except:
            print("⚠ Not a valid equation")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()