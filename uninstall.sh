if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root"
   exit 1
fi

# if [[ "$OSTYPE" == "darwin"* ]]; then
#     echo "This script is only for Linux!"
#     exit 1
# fi

clear

clear

echo -e '
    __  ___      __  __    _            ______              __                __
   /  |/  /_  __/ /_/ /_  (_)________ _/ / __ \____ ___  __/ /___  ____ _____/ /
  / /|_/ / / / / __/ __ \/ / ___/ __ `/ / /_/ / __ `/ / / / / __ \/ __ `/ __  / 
 / /  / / /_/ / /_/ / / / / /__/ /_/ / / ____/ /_/ / /_/ / / /_/ / /_/ / /_/ /  
/_/  /_/\__, /\__/_/ /_/_/\___/\__,_/_/_/    \__,_/\__, /_/\____/\__,_/\__,_/   
       /____/                                     /____/ 

'

cd .. 

sudo rm -r mythical-payload

echo 'Successfully deleted!'