from msilib.schema import File
from random import randint as rn 
from colorama import Fore as f, Back as b
from os import system
chars = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','+','=']
out = ''
File = open('output.txt','a+')
def clr():
    system('cls'or'clear')
def save():
    print(f.LIGHTGREEN_EX+"\nDo you want to save this Password? "+f.LIGHTMAGENTA_EX+"[y/n]")
    save = input()
    if save == 'y':
        print("ok, Please choose a name for your password:")
        name = input()
        File.writelines(name+" : "+out+"\n")
    if save == 'n':
        input("please press enter to quit")
## ---- # 1 # ---- ##
clr()
print(f.YELLOW+'[1]'+f.GREEN+' Create New Password')
print(f.YELLOW+'[0]'+f.GREEN+' Exit')

work = int(input("Please Select a Task: "))

if work == 1:
    clr()
    print(f.WHITE+"Password Models: ")
    print(f.MAGENTA+'[1]'+f.RED+' Average      '+f.WHITE+'8-Chars')
    print(f.MAGENTA+'[2]'+f.YELLOW+' Strong       '+f.WHITE+'12-Chars')
    print(f.MAGENTA+'[3]'+f.GREEN+' Very Strong  '+f.WHITE+'16-Chars')
    Pass_type = int(input('\nPlease Select a Model: '+f.YELLOW))
    if Pass_type == 1:
        for i in range(8):
            char = rn(0,73)
            char = chars[char]
            out = out+char
        print(f.CYAN+"Your Password is: "+f.YELLOW+out)
        save()
    if Pass_type == 2:
        for i in range(12):
            char = rn(0,73)
            char = chars[char]
            out = out+char
        print(f.CYAN+"Your Password is: "+f.YELLOW+out)
        save()
    if Pass_type == 3:
        for i in range(16):
            char = rn(0,73)
            char = chars[char]
            out = out+char
        print(f.CYAN+"Your Password is: "+f.YELLOW+out)
        save()
if work == 0:
    quit()