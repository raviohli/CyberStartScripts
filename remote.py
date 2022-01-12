import socket
import time
HOST = "services.cyberprotection.agency"
PORT = 9999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = str(s.recv(1024))
    strippedString = data.replace("\\", " ").replace("n", "").replace("b", "").replace("'", "")
    print(strippedString)
    a,b,c = strippedString.split(" ", 2)
    a = int(a)
    b = int(b)
    c = int(c)
    print(a*b)
    axb=a*b
    finalNum=axb/c
    print(finalNum)
    #print("This is the final number:" + test)
    # float tto int
    test = int(finalNum)
    print(test)
    s.sendall(bytes(str(test), "UTF-8"))
    print(s.recv(2048))

