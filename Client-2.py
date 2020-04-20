import socket

s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.connect((socket.gethostname(),2001))
print("*****************TRUCK 2 ACTIVE*************")
while True:
    k=s2.recv(1024).decode('ascii')
    if(len(k)>0):
        print(k)
    else:
        break
    z='('+k+')'+' Order Completed'
    s2.sendall(z.encode())
s2.close()
