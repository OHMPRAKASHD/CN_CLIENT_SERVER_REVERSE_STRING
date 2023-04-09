import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# Accept incoming connections
client_socket, address = server_socket.accept()

print(f'Connected by {address}')

# Receive the string from the client
data = client_socket.recv(1024).decode()

# Reverse the string
reversed_string = data[::-1]

# Send the reversed string to the client
client_socket.send(reversed_string.encode())

# Close the socket
client_socket.close()
server_socket.close()

