import os
import sys

import time
from lang_payload.check import check_os, check_root


black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

clear = lambda: os.system('clear')

clear()

check_root()

check_os()



menu = f'''{blue}
    __  ___      __  __    _            ______              __                __
   /  |/  /_  __/ /_/ /_  (_)________ _/ / __ \____ ___  __/ /___  ____ _____/ /
  / /|_/ / / / / __/ __ \/ / ___/ __ `/ / /_/ / __ `/ / / / / __ \/ __ `/ __  / 
 / /  / / /_/ / /_/ / / / / /__/ /_/ / / ____/ /_/ / /_/ / / /_/ / /_/ / /_/ /  
/_/  /_/\__, /\__/_/ /_/_/\___/\__,_/_/_/    \__,_/\__, /_/\____/\__,_/\__,_/   
       /____/                                     /____/{blue}                        
            {cyan}
                         _____________________________________
                        |Code by: mython-dev                  |
                        |Instagram: mython-dev or h4ckerworld |
                        |Github: https://github.com/mython-dev|
                         -------------------------------------  {cyan}

                              {info}Tool version 1.0

          {red}<<<<<<<<<<<<<<<<<<<<<<<<     MENU     >>>>>>>>>>>>>>>>>>>>>>>>>{red}
{nc}
{info2}{nc} OS Payloads

{yellow}[1] Windows --> Payload generate for Windows.         
{yellow}[2] Android --> Payload generate for Android.         
{yellow}[3] Linux --> Payload generate for Linux.             
                    
{info2}{nc} Language Payloads

{yellow}[4] BASH --> Payload for BASH.                         
{yellow}[5] PHP --> Payload for PHP.                               
{yellow}[6] Python --> Payload for Python.                             
{yellow}[7] Java --> Payload for Java. 
{yellow}[8] Node.js --> Payload for Node.js.
{yellow}[9] PERL --> Payload for perl.      
{yellow}[10] Ruby --> Payload for Ruby.        

{red}[q] Exit {white}[m] More Tools
'''
print(menu)

def main():

    try:
        choose_payload = input(f'{info}{nc}MythicalPayload:~# ')
    except KeyboardInterrupt:
        print(f'\n{success}Exit!\n')
        time.sleep(0.5)
        sys.exit()
    
    if choose_payload == 'q':
        print(f'\n{success}Exit!\n')
        time.sleep(0.5)
        sys.exit()

    elif choose_payload == 'm':
        print(f'\n{success}More tools in my github --> https://github.com/mython-dev/\n')
        main()
    
    elif choose_payload == '1':
        time.sleep(0.5)
        os.system('python3 os_payload/windows.py')
    elif choose_payload == '2':
        time.sleep(0.5)
        os.system('python3 os_payload/android.py')
    elif choose_payload == '3':
        time.sleep(0.5)
        os.system('python3 os_payload/linux.py')
    
    elif choose_payload == '4':
        time.sleep(0.5)
        os.system('python3 lang_payload/bash.py')

    elif choose_payload == '5':
        time.sleep(0.5)
        os.system('python3 lang_payload/php.py')

    elif choose_payload == '6':
        time.sleep(0.5)
        os.system('python3 lang_payload/python.py')

    elif choose_payload == '7':
        time.sleep(0.5)
        os.system('python3 lang_payload/java.py')

    elif choose_payload == '8':
        time.sleep(0.5)
        os.system('python3 lang_payload/node.js.py')

    elif choose_payload == '9':
        time.sleep(0.5)
        os.system('python3 lang_payload/perl.py')

    elif choose_payload == '10':
        time.sleep(0.5)
        os.system('python3 lang_payload/ruby.py')

    else:
        time.sleep(0.5)
        print(f'\n{error}Unknown command: {choose_payload}\n') 
        return main()
        
main()
