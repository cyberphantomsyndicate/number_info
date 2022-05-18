import time 
from colorama import Fore ,Back ,Style ,init 
init (autoreset =True )
def startMessage ():
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code: ")
    OOOO0OO000OO0OOOO ="Jaan"
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :
        print (Fore .RED +'[X] wrong code')
        print (Fore .BLUE +''' 
   1. Join my Telegram Group for Code 
   2. Group Link:https://t.me/Termux_official_01
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')
        startMessage ()
    else :
        print (Fore .GREEN +"Successfully Unlocked Tool!")
        pass 
if __name__ =="__main__":
    startMessage ()

from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint
#Main
a=int(input("enter first number : "))
b=int(input("enter second number : "))
print("sum of",a, "and",b,"is",a+b)
print("coded my Qadir")
