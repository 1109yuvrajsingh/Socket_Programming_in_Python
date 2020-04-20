import socket

s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.connect((socket.gethostname(),2002))
print("*****************TRUCK 3 ACTIVE*************")
while True:
    k=s3.recv(1024).decode('ascii')
    if(len(k)>0):
        print(k)
    else:
        break
    z='('+k+')'+' Order Completed'
    s3.sendall(z.encode())
s3.close()
