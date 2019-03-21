#Lab02
#Colin Kelleher (117303363)

# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# the machine address and port number have to be the same as the server is using.
hostname = gethostname() #get the hostname
ip = gethostbyname(hostname) #get the IP address
server_address = (hostname, 10000) #hostname and port values, can be changed according to server
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
print('IP address %s' % ip) #print the IP address
# Connect the socket to the host and port
sock.connect(server_address)

while True: #while the following is true
    try:
        message = input('Person 1: ') #input message from person 1
    except: #otherwise if input incorrect
        print('Message was inputted incorrectly - try again') #print error message
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        # Change encoding from 16-bit to 64-bit
        data = sock.recv(64).decode()
        amount_received += len(data)
        # Print the server message to screen
        print('%s' % data)

# If client is no longer connected to the server, close the connection
else:
    print('closing socket')
    sock.close() #close