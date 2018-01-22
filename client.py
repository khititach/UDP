import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
num = int(raw_input("Enter number: "))
MESSAGE = str(num)

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
