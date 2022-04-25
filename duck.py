import netifaces
import requests
from os import environ
from dotenv import load_dotenv

load_dotenv()



netifaces.interfaces()
addrs = netifaces.ifaddresses("wlp3s0")
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
print(response.status_code, response.text,response.url,environ.get("DOMAINS"))
