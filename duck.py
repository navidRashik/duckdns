import imp
import netifaces
import requests
from os import environ
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
load_dotenv()

print("-----------------Starts---------------------",datetime.now())
pprint(netifaces.interfaces())
addrs = netifaces.ifaddresses("wlp3s0")
pprint(addrs)
ipv6 = addrs[netifaces.AF_INET6][0]["addr"]
print(ipv6)
response = requests.get(
    url="https://www.duckdns.org/update",
    params={
        "token": environ.get("TOKEN"),
        "domains": environ.get("DOMAINS"),
        "ipv6": ipv6,
    },
)

# response = requests.get(url="https://www.duckdns.org/update?domains=navidrashik&token=bb26ad54-9c69-41d7-b524-908ca10e515e&ip=")
pprint(
    {
        "status_code": response.status_code,
        "response_txt": response.text,
        "url": response.url,
        "doman_name": environ.get("DOMAINS"),
    }
)
