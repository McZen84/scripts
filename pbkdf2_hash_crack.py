import hashlib
import binascii
from pwn import log

# Parameters from gitea.db
salt = binascii.unhexlify('227d873cca89103cd83a976bdac52486')
key = '97907280dc24fe517c43475bd218bfad56c25d4d11037d8b6da440efd4d691adfead40330b2aa6aaf1f33621d0d73228fc16'
dklen = 50
iterations = 50000

# Hashes a password using PBKDF2 from wordlist.
def pbkdf2_hash(password, salt, iterations, dklen):
    hash_value = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password = password,
        salt = salt,
        iterations = iterations,
        dklen = dklen
    ) 
    return hash_value

# Cracking password
dict = '/home/kali/rockyou.txt'
passwd_found = False

with open(dict, 'r', encoding='utf-8') as file:
    for line in file:
        password = line.strip().encode('utf-8') 
            
        # Generate hash
        hash_value = pbkdf2_hash(password, salt, iterations, dklen)

        # Convert target hash to hex
        target_hash_bytes = binascii.unhexlify(key)
    
        # Check for match
        if hash_value == target_hash_bytes:   
            print(f'Found password: {password}!')
            passwd_found = True
            break
               
    if not passwd_found:
        print("Not found.")

    
