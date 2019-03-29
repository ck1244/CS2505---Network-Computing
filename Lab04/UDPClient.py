#Lab04
#UDPClient.py
#Colin Kelleher - 117303363

# import sys to be able to take in command line arguements
import sys

# from the socket module import all
from socket import *

# Create a UDP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_DRGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)

# Take argument from command line and assign to hostname
server_host = sys.argv[1]
# get hostname of machine and store in hostname
ip = gethostbyname(server_host)
# Assign a port number
serverPort = 6789

# python3 UDPClient.py hostname

# server_address corresponds to the inputted argument in command line & server port number
server_address = (ip, serverPort)

# Try send message to server
try:
    # take string from user through terminal and assign to data
    data = input('Please enter your message to be converted to upper case: ')
    print('sending "%s"' % data) #print what you are sending to srver
    #encode data and send to the server
    sock.sendto(data.encode(), (server_address))

    # Look for the response
    amount_received = 0
    amount_expected = len(data)

    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        received_data, address = sock.recvfrom(1024)
        # decode() returns string object
        received_data = received_data.decode()
        amount_received += len(received_data)
        #print upper case string to screen
        print('received: ' + received_data)

# used for error handling - prints message if error occurs within body of code
except IOError:
    print('Error - please try again')

# close socket when finished
finally:
    print('** closing socket **')
    sock.close()