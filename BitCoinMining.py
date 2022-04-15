import os
from hashlib import sha256
import time

done = False
MAX_NONCE = 100000

ans = input("Do you want to clear the terminal first? (y/n) :")
if ans == 'y':
    new_hash = ""
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    new_hash = ""

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    new_hash = ''
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with value:{nonce}")
        return new_hash

    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")
    
old_hash = '7d11d48a006a7b61d66946c7b5ae345532a2ff7a61a341dae2c10797c8bec9e4'
if __name__=='__main__':
    
    transactions='''
    jerri->cindy->20,
    cindy->jerri->45,
    randy->jerri->35
    '''
    difficulty = 4
    start = time.time()
    new_hash = mine(5,transactions, old_hash, difficulty)
    total_time = str((time.time() - start))
    print(f"End mining. Mining took: {total_time} seconds")
    print(new_hash)

    while (done == False):
        ans = input("Try again? (y/n) : ")

        if ans == 'y':
            mine(5,transactions,new_hash,difficulty)
        else:
            done = True