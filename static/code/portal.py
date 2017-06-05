# Import this library
import helper

# This is the hostname and port to use.
server = '127.0.0.1'
port = 8888

# This list lets us know that the server wants a response
send_list = ["?"]

# Connection to hostname on the port.
helper.open_connection(server, port)

# Set the max messsage size
max_message_size = 1024

# Receive the first message
server_message = helper.client_receive_message()

# Print the first message
print("Got message from server: " + server_message)

# Infinite loop, go as long as possible
while True: 
    # Wait for message from the server
    server_message = helper.client_receive_message()

    # Disconnect from the server if it says goodbye
    if server_message == 'goodbye':
        print("Disconnecting from server.")
        break

    # Print the server message
    print("Server Message: " + server_message)

    # If the message contains an item from the send list, send a response
    if any(word in server_message for word in send_list):
         message = input()
         helper.client_send_message(message)
    
# Close the connection
helper.close_client()
