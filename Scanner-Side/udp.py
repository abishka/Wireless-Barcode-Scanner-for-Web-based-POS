import socket

localIP     = "192.168.25.10"
localPort   = 4210


MESSAGE = b"Hello, World!"

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (localIP, localPort))


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind(('0.0.0.0', 4211))
while True:
    data, addr = UDPServerSocket.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message: %s" % data)
