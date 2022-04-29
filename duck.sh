
# echo url="https://www.duckdns.org/update?domains=navidrashik&token=bb26ad54-9c69-41d7-b524-908ca10e515e&ip=" | curl -k -o ~/duckdns/duck.log -K -
sudo apt install python3-pip
pip install requests netifaces python-dotenv && python3 duck.py > duck.log 