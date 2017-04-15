import socket
import sys
import struct
import ReportProcessor

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 8888)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            recvData = connection.recv(13)
            dataToUnpack = recvData[4:]
            ieeeAddress, occupancyState = struct.unpack('QB', dataToUnpack)
            print "Source IEEE address: %016x" % ieeeAddress
            if recvData:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(recvData)
                ReportProcessor.raw_report_handler(ieeeAddress, occupancyState)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()

socket.close()
