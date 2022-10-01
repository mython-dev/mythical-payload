
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root"
   exit 1
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "This script is only for Linux!"
    exit 1
fi

clear

echo -e '
    __  ___      __  __    _            ______              __                __
   /  |/  /_  __/ /_/ /_  (_)________ _/ / __ \____ ___  __/ /___  ____ _____/ /
  / /|_/ / / / / __/ __ \/ / ___/ __ `/ / /_/ / __ `/ / / / / __ \/ __ `/ __  / 
 / /  / / /_/ / /_/ / / / / /__/ /_/ / / ____/ /_/ / /_/ / / /_/ / /_/ / /_/ /  
/_/  /_/\__, /\__/_/ /_/_/\___/\__,_/_/_/    \__,_/\__, /_/\____/\__,_/\__,_/   
       /____/                                     /____/ 

'
# Update packet and Install python & pip

sudo apt update && sudo apt upgrade -y && sudo apt install python3 && sudo apt install python3-pip

# install sockets

pip3 install sockets

# install metasploit 

curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall

# clear terminal

clear



sudo python3 mythicalpayload.py
