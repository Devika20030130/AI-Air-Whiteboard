# AI Whiteboard v2 🎨🤖

An AI-powered virtual whiteboard built using **OpenCV**, **MediaPipe**, **Tesseract OCR**, and **SymPy**.  
Draw in the air using hand gestures, recognize handwritten expressions, and solve mathematical equations in real time.

---

## ✨ Features

- ✍️ Air drawing using hand tracking
- 🖐️ Gesture-based controls
- 🧠 OCR text recognition using Tesseract
- ➗ Mathematical expression solving using SymPy
- 🧹 Clear canvas gesture
- 👍 New line gesture
- 📷 Real-time webcam interaction

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- PyTesseract
- SymPy

---

# 📂 Project Structure

```bash
AI-Whiteboard-v2/
│
├── main.py
├── drawing.png
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Whiteboard-v2.git
cd AI-Whiteboard-v2
```

---

## 2️⃣ Create Virtual Environment (Optional but Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install opencv-python mediapipe numpy pytesseract sympy
```

---

# 🔧 Install Tesseract OCR

Download and install Tesseract OCR:

- Windows: https://github.com/UB-Mannheim/tesseract/wiki

### Linux

```bash
sudo apt install tesseract-ocr
```

---

## Update Tesseract Path

In `main.py`, update:

```python
pytesseract.pytesseract.tesseract_cmd = r"D:\New Program Files\tesseract.exe"
```

with your own Tesseract installation path.

Example:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🖐️ Gesture Controls

| Gesture | Action |
|---|---|
| ☝️ Index Finger Up | Draw |
| ✌️ Index + Middle Finger Up | Space / Stop Drawing |
| ✊ Closed Hand | Clear Canvas |
| 👍 Thumb Up | New Line |

---

# ⌨️ Keyboard Controls

| Key | Function |
|---|---|
| `r` | Recognize & Solve Equation |
| `q` | Quit Application |

---

# 🧠 Example

Draw:

```text
2 + 3 * 5
```

Press:

```text
r
```

Output:

```text
➗ Result: 17
```

---

# 📸 Future Improvements

- Multi-color drawing
- Shape recognition
- AI handwriting enhancement

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 👨‍💻 Author

Developed by **Devika** 🚀  
ECE Student | AI Tool Explorer | GenAI Enthusiast 🤖
