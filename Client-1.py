import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((socket.gethostname(),2000))
print("*****************TRUCK 1 ACTIVE***************")
while True:
    k=s1.recv(1024).decode('ascii')
    if(len(k)>0):
        print(k)
    else:
        break
    z='('+k+')'+' Order Completed'
    s1.sendall(z.encode())
s1.close()
