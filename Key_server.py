import socket

HOST = '0.0.0.0'
PORT = 65437

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("listening on: " + HOST + ":" + str(PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected by: " + str(addr))
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                break