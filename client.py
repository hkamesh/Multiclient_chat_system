import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port number

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            break

# Main client function
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
