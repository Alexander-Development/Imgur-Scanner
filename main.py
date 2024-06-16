import requests
import threading
import random
import colorama
import os

valid = 0
invalid = 0

os.system(f'title "[Imgur Scanner] By Alex | Invalid: {invalid} | Valid: {valid}"')

def check():
    global valid, invalid
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        url = "https://imgur.com/" + ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcbnm123456789') for i in range(7))
        response = requests.get(url, headers=headers)
        if '<title>Imgur: The magic of the Internet</title>' in response.text:
            print(f"{colorama.Fore.GREEN}{url}{colorama.Fore.RESET}")
            valid += 1
        else:
            invalid += 1
        os.system(f'title "[Imgur Scanner] By Alex | Invalid: {invalid} | Valid: {valid}"')
    except:
        pass

def main():
    while True:
        check()

for i in range(200):
    threading.Thread(target=main).start()
