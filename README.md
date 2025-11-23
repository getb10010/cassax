# Auto Typer Script

This Python script automates typing a message repeatedly using **PyAutoGUI**. It types your text into the active window and presses **Enter** after each message.

---

## 🚀 Features

* Automatically types a message any number of times.
* Presses `Enter` after each message.
* Allows a custom delay before starting.
* Simple, beginner-friendly interface.

---

## 📦 Requirements

Install dependencies via:

```bash
pip install -r requirements.txt
```

### requirements.txt

```
pyautogui
```

---

## 📝 Usage

1. Run the script:

```bash
python auto_typer.py
```

2. Enter the text you want to send:

```
ENTER THE TEXT:
```

3. Enter how many times it should repeat:

```
HOW MUCH =
```

4. Enter how many seconds to wait before starting:

```
HOW MUCH I SHOULD WAIT =
```

5. Switch to the window where you want the message typed.

---

## ⚠️ Warning

* **PyAutoGUI controls your keyboard**, so keep the target window active.
* Do NOT use this script for spam or breaking platform rules.
* Move your mouse to a screen corner to trigger PyAutoGUI's failsafe.

---

## 🧩 Example

If you enter:

```
ENTER THE TEXT: hello
HOW MUCH = 5
HOW MUCH I SHOULD WAIT = 3
```

The script waits 3 seconds, then types:

```
hello
hello
hello
hello
hello
```

---

## 📜 License

This project is free to modify and use for educational and personal purposes.
