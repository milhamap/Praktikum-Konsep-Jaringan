import socket              # Import socket module

s = socket.socket()        # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345           # Reserve a port for your service.

s.connect((host, port)) # Connect to the server
print(s.recv(1024)) # Receive no more than 1024 bytes
s.close()      # Close the socket when done