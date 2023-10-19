import socket
server_ip = "127.0.0.1"  # Địa chỉ IP của server
server_port = 8890       # Cổng của server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

while True:
    data1 = input("Nhập chuỗi số nguyên (cách nhau bởi khoảng trắng): ") 
    if data1 != '.':
        file = open("data.txt", "a")
        file.write(data1 + "\n")
    with open("data.txt", "r") as file:
        data = file.read()
    if data1 == '.':
        break

client.send(data.encode())
result = client.recv(1024).decode()
print(f"Tổng = {result}")