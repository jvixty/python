import time
import webbrowser
import os
import random
import socket


print("Hacking started")
time.sleep(1)
print("Hacking in progress...")
a=0
b=random.randint(1,3)
c=random.randint(1, 4)
if b == 1:
    for i in range(100):
        time.sleep(0.1)
        print('hacking [%d%%]\r'%i, end="")
   
    print("hacking ended succesfully")
    webbrowser.open('https://lublin.eu/lublin/o-miescie/lublin-na-zywo/', new=2)

if b == 2:
    while a<101:
        print(a)
        a=a+20
        time.sleep(0.5)
    time.sleep(1)
    print("hacking failed")
    
if b ==3:
    print("you got hacked")
    if c==1:
        os.system('shutdown /p')
    if c==2:
        webbrowser.open('http://fakebsod.com/windows-8-and-10', new=2)
    if c==3:
        os.mkdir("C:\PY.dir.3")
    if c==4:
       print("hello")
       print(os.getlogin())
       hostname = socket.gethostname()
       ip_address = socket.gethostbyname(hostname)
       print(f"IP Address: {ip_address}")
       
