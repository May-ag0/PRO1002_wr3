import socket



hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hello! Your IP address is: ",ip_address)