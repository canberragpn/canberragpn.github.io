# Import the required library
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Open the connection from the client side
def open_connection(serverip, port):
	# connection to hostname on the port.
	client_socket.connect((serverip, port))

# Have the client recieve the message
def client_receive_message():
	max_message_size = 1024
	data = client_socket.recv(max_message_size) #got bytes but have to convert to string
	server_message = data.decode('ascii')
	return server_message

# Have the client send the message
def client_send_message(message):
        message = str(message)
        message_bytes = message.encode('ascii')
        client_socket.send(message_bytes)

# Have the server send a message
def send(connection, message):
        message_encoded = None
        message_encoded = message.encode('ascii')
        connection.send(message_encoded)

# Have the server receive a message
def receive(connection):
        max_message_size = 1024
        data = connection.recv(max_message_size)
        message = data.decode('ascii')
        return message

# Close the connection
def close_client():
	client_socket.close()

# Close the server
def close(connection):
        send(connection, 'goodbye')
        client_socket.close()
        connection.close()

# Have the server bind to the socket
def bind(server_ip, server_port):
        client_socket.bind((server_ip, server_port))

# Have the server listen for a number of connections
def listen(conn_number):
        client_socket.listen(conn_number)

# Have the server accept a connection
def accept():
        connection, address = client_socket.accept()
        return connection



def ask_question(connection, message):
        send(connection, message)
        return receive(connection)

def test(num1, num2):
        return num1 + num2
