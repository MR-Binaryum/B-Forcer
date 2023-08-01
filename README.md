# B-Forcer

B-Forcer its a software writted on Python to cracking passwords  that are encoded by hash algoritms.

The graphical interface its easy to use, when you start the program they shows you avalaible algoritms to crack hashes then after that the software launches you a message that is to put the hash that you want to crack. 

(Like this)

![crack1](https://github.com/MR-Binaryum/B-Forcer/assets/133718570/a4e3e19c-feeb-4198-a30a-4d61e67d9a1a)



So when you press enter key after paste or writted the hash then starts the Brute force attack.

And it presents the special part of this program  that its the stetic like a hollywood hacker movie :)

![crack2](https://github.com/MR-Binaryum/B-Forcer/assets/133718570/9bac84e8-8fe4-42b5-b676-755f8e1a99ef)



One last thing if you want to change the Brute Force diccionary or the algoritm to crack go to this lines...

    wordlist = open("upload.txt", "r")
                        |
                        |_ Diccionary name
                        
  wordlist = open("numer4-5.txt", "r") --> Example with another Diccionary...
    
  --------------------------------------------------------------------------------------------------------------
            
            
            crypted_password = hashlib.sha256(word.encode()).hexdigest() 
                                        |
                                        |__ Default algoritm in the menu you have the other algoritm that you can use...
                                         
               
            crypted_password = hashlib.sha512(word.encode()).hexdigest() --> Example with another Algoritm...
            
####Requeriments for the software####

Brute force diccionary in format .txt

####Requeriments####

git 

python3

####EXECUTE#######

git clone https://github.com/MR-Binaryum/B-Forcer.git

cd B-Forcer

sudo python3 B-Forcer.py
