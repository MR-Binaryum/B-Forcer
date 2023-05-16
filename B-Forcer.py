import colorama
from colorama import Fore, Style
import hashlib
import time

hashList=['MD5 ','SHA1 ','SHA224 ', 'SHA256 ', 'SHA334 ', 'SHA512 ' ]

print("")
print("Avalaible Hashes to CRACK")
print("______________________________________________")
print(''.join(hashList))
print("----------------------------------------------")
print("")


def hashCrack():
    print("")
    print("")
    hash_name = input("[+] Enter the HASH target: ")
    print("")

    wordlist = open("upload.txt", "r")

    for word in wordlist.readlines():
        word = word.strip()
        crypted_password = hashlib.sha256(word.encode()).hexdigest()
        if hash_name == crypted_password: 
            print(Style.BRIGHT+Fore.GREEN + "[+] Password Cracked: " +word + "    hash: " +crypted_password + "    [STATUS] Verification SUCCESFULL(√)")
            print("")
            break
        else:
            time.sleep(0.0003)
            print(Fore.RED + "[-] Incorrect password: " +word  +"         hash: "  +crypted_password + "        [STATUS] Verification FAILED(X)")
hashCrack()
