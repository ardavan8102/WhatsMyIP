import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
init()

url = "https://www.google.com/search?q=what+is+my+ip&rlz=1C1GGRV_enIR901IR901&oq=what+is+my+ip&aqs=chrome..69i57j0i512l9.3824j0j7&sourceid=chrome&ie=UTF-8"

source = requests.get(url)
content = BeautifulSoup(source.content, 'html.parser')

ip = content.find('span', class_= "r0bn4c rQMQod") # IPv4

print("Your IP : " + Fore.LIGHTRED_EX + ip.text + Fore.WHITE)