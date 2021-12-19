import socket
import struct
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', MCAST_PORT))
merq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, merq)

while True:
   mesaj = sock.recv(10240).decode('utf-8')
   print(mesaj)
   break

sock.close()