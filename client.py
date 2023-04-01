import socket
c_Addr = "127.1.1.1"
c_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (c_Addr, 1234)
c_Choice = "Y"
while c_Choice.upper() == "Y":
    domain_input = input("Enter domain name : ")
    send = c_Socket.sendto(domain_input.encode(), addr)
    data, address = c_Socket.recvfrom(512)
    cname, address = c_Socket.recvfrom(512)
    server_reply = data.decode().strip()
    cname_reply = cname.decode().strip()
    message = "The IP of the " + format(cname_reply)+" server is " + format(server_reply)
    print(message)
    c_Choice = (input("Do you want to continue?(y/n)"))
c_Socket.close()