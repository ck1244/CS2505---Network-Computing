# Lab05
# Colin Kelleher
# 117303363
# Terminal input = python3 ** UDP_ping_client.py 10 localhost **

# import statistics to carry out std-dev
import statistics
# Import the socket module
from socket import *
# Import the time module to calculate the time
from time import *
# Import the sys module to take terminal input
import sys

# Create a UDP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_DRGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)
# Take argument from command line and assign to hostname
pingNo = int(sys.argv[1])
# Take argument from command line and assign to server_host
server_host = sys.argv[2]

# Get the host name and ip address
ipaddr = gethostbyname(server_host)
# Assign a port number
serverPort = 12000

# Assign server_address using ipaddr and server port as above
server_address = (ipaddr, serverPort)
# Set the timeout length - 1 second as per assignment
sock.settimeout(1)

# keeps count of the total number of packets received
total_packets = 0

# Variable to keep track of the sequence number
seq = 0

# printing out the start of the Ping format
print("PING %s: %i data packets" % (ipaddr, pingNo))

# create a list which will hold the times, for calculations
times = []

# While the sequence number is less than the ping number
while seq < pingNo:
    try:
        # Set the start time
        startTime = time()
        # Increment sequence number by 1
        seq += 1
        # create the ping message as below
        ping = " Ping %s from %s" % (seq, ipaddr)

        # Send ping to server
        sock.sendto(ping.encode(), server_address)

        # Receive response from the server
        data, server = sock.recvfrom(1024)

        # start timer to get end-time
        endTime = time()
        # Calculate the round trip time (end time minus start time)         (RTT)
        totalTime = (endTime - startTime) * 1000
        # append the times to the list
        times.append(totalTime)
        # Print the response to screen - formatted as per assignment
        print(data.decode() + " udp_seq = %s, time = %.3fms" % (str(seq), (totalTime)))

        # counts the number of received packets
        total_packets = total_packets + 1
    # If the connection times out, print error to screen
    except timeout:
        print("Request timed out")

# calculate the packet loss - number of pings minus number of received packets divided by number pings . multiply by
# 100 for percentage
packetLoss = ((pingNo - total_packets) / pingNo) * 100

# printing the output as per the assignment
print("--- %s ping statistics ---" % ipaddr)
print(" %i packets transmitted, %i packets received, %.2f %% packet loss" % (pingNo, total_packets, packetLoss))
average = sum(times) / len(times)
print("round-trip min/avg/max/stddev = %.3f/%.3f/%.3f/%.3f ms" % (
min(times), average, max(times), statistics.stdev(times)))

# Close socket
sock.close()
