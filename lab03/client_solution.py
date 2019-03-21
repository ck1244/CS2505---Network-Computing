# Lab03


# sys is imported to be able to take in command line arguments
import sys
# from the socket module import all
from socket import *
# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# Take arguments from command line and assign them to variables
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]
# client.py server_host server_port filename
# server_address corresponds to the inputted arguments in command line
server_address = (server_host, int(server_port))
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)

# Connect the socket to the host and port
sock.connect(server_address)
# after connecting, try to run the following code
try:
    # Send data
    # Send the GET request to the server
    httpRequest = ("""GET /%s HTTP/1.1 """ % (filename))
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(httpRequest.encode())

    data = True

    # while there is data present
    while data:
        # Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(64).decode()
        # Print the web page to the screen
        print('%s' % data, end='')

# If there is no longer a connection, close the connection
except IOError:
    print('Error with connection')

finally:
    print('closing socket')
    # close the connection

    sock.close()
