#Lab02

# from the socket module import all
from socket import *
from datetime import * #date and time imported for file use
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

#get the hostname
hostname = gethostname()
#get the IP address
ip = gethostbyname(hostname)

#input the server address
server_address = (hostname, 10000)
# output to terminal some info on the address details
print('*** IP Address = %s ***' % ip) #print IP address
#Print server address
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

#while the following is true, keep running the code (always true so server is always running)
while True:
#print message that server is waiting for an connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    
    try: #try run the following code, print the client address
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True: #run the following code while it its true
            # decode() function returns string object
            #increase the qty from 16 to 64 for this assignment
            data = connection.recv(64).decode()
            if data: #if data present
                dateAndTime = str(datetime.now()) #get the date and time
                file = open('logfile.txt', 'a') #open a text file ready to 'append' to
                #write the follwing message: data, date and time
                file.write('Person1: ' + data + ' Date & Time:' + dateAndTime + '\n') #write the message from client to file
                print('Person 1: %s' % data) #print message from client to screen
                data2 = input('Person2: ') #take an input message on server
                file.write('Person2: ' + data2 + 'Date & Time:' + dateAndTime + '\n') #write it to the file
                file.close()      #close the file
                response = ('Person1: %s' % data2)
                # encode() function returns bytes object
                connection.sendall(response.encode())
                # encode() function returns bytes object
            else:
                print('no more data from', client_address) #‚rint message
                break
    except IOError: #Error with data
        print('no more data from', client_address) #print Message
        pass


    finally:
        # Clean up the connection
        connection.close() #close connection

# now close the socket
sock.close()
