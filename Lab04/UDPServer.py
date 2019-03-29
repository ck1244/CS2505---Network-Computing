#Lab04
#UDPServer.py
#Colin Kelleher - 117303363

# from the socket module import all
from socket import *
# from datetime import all - used for writing to file
from datetime import *

# Create a UDP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_DGRAM is used for UDP)
# changed from SOCK_STREAM used for TCP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# get hostname of machine
hostname = gethostname()
# Assign a port number
serverPort = 6789

# Assign server_address from client & server port
server_address = ("", serverPort)

print('** starting server at %s port %s **' % server_address)
# Bind the socket to server address and server port
serverSocket.bind(server_address)


# While the following is true
while True:
try:
    print(' ** Waiting for messages **')
    # Extract address and port of the client
    data, client_address = serverSocket.recvfrom(1024)
    # decode the data
    data = data.decode()
    if data:
        #print the data to the screen
        print("Received: %s" % data)
        # Get the date and time
        date_time = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
        # Open a log file with append properties
        log_file = open('logfile.txt', 'a')
        # write the upper case message and date and time to file
        log_file.write('Message: ' + data.upper() + ' Date & Time: ' + date_time + '\n')
        # Close the log file
        log_file.close()
        # change data to upper case and send upper case data + date and time back to client
        data = "%s %s" % (data.upper(), date_time)
        # Send the data back to the client
        print("Sending: " + data)
        serverSocket.sendto(data.encode(), client_address)
    else:
        serverSocket.close() #close socket
        break
except:
	print('Error, please try again)
    # Close the socket

