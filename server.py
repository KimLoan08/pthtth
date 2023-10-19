import socket

def calculate_sum(data):
    numbers = [int(num) for num in data.split()]  
    results = sum(numbers)  
    return results 


def main():
    server_ip = "127.0.0.1"  # Địa chỉ IP của server
    server_port = 8890       # Cổng của server

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print("Server đang lắng nghe...")

    while True:
        client_socket, addr = server.accept()
        print(f"Kết nối từ {addr[0]}:{addr[1]}")
        result = 0
        while True:  
                data = client_socket.recv(1024).decode()
                print("Dữ liệu từ client: " + data)
                result += calculate_sum(data)
                ketqua = str(result)
                print("Kết quả: " + ketqua)
                client_socket.send(ketqua.encode())  

if __name__ == "__main__":
    main()