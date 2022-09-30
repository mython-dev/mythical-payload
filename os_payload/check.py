import os
import sys
from sys import platform
import time
from pathlib import Path

clear = lambda: os.system('clear')

directory = (Path.home())

def check_os():
      os = platform      
      if os == 'win'.lower() and 'win32'.lower():
            time.sleep(0.5)
            clear()
            print(f'\nThis script is for Linux only!\n')
            sys.exit()

    #   elif os == 'darwin'.lower():
    #         time.sleep(0.5)
    #         clear()
    #         print(f'\nThis script is for Linux only!\n')
    #         sys.exit()

check_os()

def check_root():
    if os.geteuid() != 0:
        print("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
        sys.exit()

check_root()