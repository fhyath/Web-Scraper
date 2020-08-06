import os
import requests
import time
from bs4 import BeautifulSoup
from twilio.rest import Client
URL = 'https://www.ebay.com/itm/LG-G8X-ThinQ-LMG850UM9-128GB-Black-Sprint-T-mobile-AT-T-9-10-GSM-Unlocked/184231626558?epid=22035385565&hash=item2ae50f873e:g:5ZsAAOSwDuleEg3R:sc:USPSFirstClass!30087!US!-1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="prcIsum").get_text()

    converted_price = float(price[4:7])
    print(converted_price)

    if(converted_price<3000):
        send_text()


def send_text():
    account_sid = '*****' # Found on Twilio Console Dashboard
    auth_token = '*****' # Found on Twilio Console Dashboard

    myPhone = '*****' # Phone number you used to verify your Twilio account
    TwilioNumber = '+*****' # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
    to=myPhone,
    from_=TwilioNumber,
    body='The price of LG G8 has dropped')


check_price()
