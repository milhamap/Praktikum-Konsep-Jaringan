import socket            # Import socket module

s = socket.socket();      # Create a socket object
host = socket.gethostname();    # Get local machine name
port = 12345;         # Reserve a port for your service.
s.bind((host, port));   # Bind to the port

s.listen(5);    # Now wait for client connection.
while True:     # Establish connection with client.
    c, addr = s.accept();   # print 'Got connection from', addr
    print('Got connection from', addr);  # send a thank you message to the client.
    c.send('Thank you for connecting'); # Close the connection
    c.close();  # Close the connection