import time
import os
import random
import wifi
import socketpool
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_httpserver import Server, Request, Response, POST
from utils import url_decode  # Import the utility function
from humanType import type_like_human

# Set up HID
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Connect to network
print("Connecting to WiFi")
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
print("Connected to WiFi")

# Set up server
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

def serve_html_file():
    try:
        with open('/index.html', 'r') as file:
            html = file.read()
        print("Served HTML file successfully.")
        return html
    except Exception as e:
        print("Failed to read the HTML file:", e)
        return "<h1>Error loading the page</h1>"

def preprocess_text(text):
    """Normalize all types of line breaks to Unix style (newline)."""
    return text.replace('\r\n', '\n').replace('\r', '\n')

@server.route("/")
def base(request: Request):
    print("Received GET request")
    return Response(request, serve_html_file(), content_type='text/html')

@server.route("/", POST)
def handle_post(request: Request):
    print("Received POST request")
    try:
        body_start_idx = request.raw_request.index(b'\r\n\r\n') + 4
        post_data = request.raw_request[body_start_idx:]
        text = parse_post_data(post_data.decode('utf-8')) if post_data else ""
        text = preprocess_text(text)  # Assuming you have this function to normalize line breaks
        print(f"Received text to type: '{text}'")

        # Introduce a delay as explained in the HTML
        time.sleep(5)
        type_like_human(text)  # Type out the text with human-like variations including pauses
        print("Text typed out successfully.")

    except Exception as e:
        print(f"Error processing POST request: {e}")

    return Response(request, serve_html_file(), content_type='text/html')

def parse_post_data(data):
    parts = data.split('&')
    for part in parts:
        key_value = part.split('=')
        if key_value[0] == 'text':
            return url_decode(key_value[1])
    return ""

print("Starting server...")
try:
    server.start(str(wifi.radio.ipv4_address))
    print(f"Listening on http://{wifi.radio.ipv4_address}:80")
except OSError:
    print("Error starting the server, restarting...")
    time.sleep(5)
    microcontroller.reset()

while True:
    try:
        server.poll()
    except Exception as e:
        print(f"Error while polling server: {e}")
