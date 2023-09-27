try:
    import urequests as requests
except:
    import requests

import random
import time
import network
import gc

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect("Wokwi-GUEST", '')
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())

do_connect()

phone_number = '+923142351508'
# Your callmebot API key
api_key = '9869456'

def send_message(phone_number, api_key, message):
    # Set your host URL
    url = 'https://api.callmebot.com/whatsapp.php?phone='+phone_number+'&text='+message+'&apikey='+api_key
    try:
        # Make the request to send a WhatsApp message
        response = requests.get(url)
        if response.status_code == 200:
            print('WhatsApp message sent successfully!')
        else:
            print('Waiting for 10 second')
        response.close()
    except Exception as e:
        print('Error occurred while sending WhatsApp message:', str(e))

if __name__ == "__main__":
    while True:
        try:
            # Send a WhatsApp message
            message = 'Hello%20This%20is%20testing%20message%20service%0Aby%20ESP32'
            send_message(phone_number, api_key, message)
            gc.collect()
            time.sleep(10)  # Adjust the delay as needed
        except KeyboardInterrupt:
            break

network.WLAN(network.STA_IF).disconnect()