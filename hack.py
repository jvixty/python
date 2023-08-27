import time
import webbrowser
import random
import os


print("Hacking started")
time.sleep(1)
print("Hacking in progress...")
a=0
b=random.randint(1, 1)
c=random.randint(1, 4)
if b == 1:
   for i in range(100):
    time.sleep(0.1)
    print('hacking [%d%%]\r'%i, end="")
print("hacking ended succesfully")
time.sleep(1)
webbrowser.open('https://lublin.eu/lublin/o-miescie/lublin-na-zywo/', new=2)
if b == 2:
    while a<101:
        print(a)
        a=a+20
        time.sleep(0.5)
    time.sleep(1)
    print("hacking failed")
if b ==3:
    time.sleep(c)
    print("you got hacked!")
    time.sleep(5)
    os.system("shutdown /p")
