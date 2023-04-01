import socket
dns_table = {"www.youtube.com": "208.65. 153.238",
             "www.linkedin.com": "192.168.1.4",
             "www.netflix.com": "41.71. 110.82",
             "www.myntra.com": "104.123.201.31"}

cname_record={"www.youtube.com": "host.youtube.com",
              "www.linkedin.com": "host.linkedin.com",
              "www.netflix.com": "host.netflix.com",
              "www.myntra.com": "host.myntra.com"}
c_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("The server is active: ")
c_Socket.bind(("127.1.1.1", 1234))
while True:
    data, address = c_Socket.recvfrom(512)
    message = format(address) + " request for data retrieval "
    print(message)
    data = data.decode()
    ip = dns_table.get(data, "not found !").encode()
    cname = cname_record.get(data,"requested").encode()
    send = c_Socket.sendto(ip, address)
    send1 = c_Socket.sendto(cname,address)
