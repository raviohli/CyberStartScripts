import socket


HOST = "services.cyberprotection.agency"
PORT = 3166

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("connecting...")
    s.connect((HOST, PORT))
    print("connected!")
    print(s.recv(1024))
    s.send(bytes("0", 'utf-8'))
    print(str(s.recv(1024)).replace("b", "").replace("'", ""))
    s.send(bytes("firstNum", 'utf-8'))
    print(str(s.recv(1024)).replace("b", "").replace("'", ""))
