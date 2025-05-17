# Python-shell
Simple Python  Shell using sockets
# Python Reverse Shell

A simple reverse shell written in Python using `socket` and `subprocess`.

## 🔧 How It Works

- Victim runs the `victim-side.py` file.
- Attacker runs `python-shell.py` to receive a connection.
- Attacker can send commands; client executes and returns output.

## 🚀 Skills Used

- Python sockets
- Subprocess module
- Networking basics
- Blind  shell logic

## 📁 Files

- `victim-side.py`: Code that runs on the victim machine
- `python-shell.py`: Code attacker uses to interact with the victim
