import socket
group = '224.1.1.1'
port = 5003
ttl = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


sock.sendto(b"hello world from server!!!", (group, port))
sock.close()