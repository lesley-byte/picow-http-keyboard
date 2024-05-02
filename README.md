# Pico W HID Typing System

![Static Badge](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

This project harnesses the power of the Raspberry Pi Pico W to operate a human interface device (HID) that types out text input from a web interface in a human-like manner. It showcases how the Pico W can be used for network communication and real HID operations through USB.

## Features

- WiFi Connectivity: Automatically connects to a specified WiFi network using environment variables for credentials.
- HTTP Server: Runs a web server that handles GET and POST requests, allowing users to interact with the device via a web page.
- Human-like Typing: Types on a USB keyboard with variable speed and accuracy to mimic human typing, including intentional typos and corrections.

## Setup and Installation

### Hardware Requirements

- [Raspberry Pi Pico W](https://www.adafruit.com/product/5526)

### Software Requirements

- [MU Editor](https://codewith.mu/)
- [CircuitPython](https://circuitpython.org/)
- Install the **required libraries** ( `adafruit_hid`, `adafruit_httpserver` ) [Adafruit CircuitPython Libraries](https://circuitpython.org/libraries)

### Wifi Configuration

- update `settings.toml` with your wifi credentials

### Installation

1. Clone this repository: `git clone`
2. copy the contents to your Pico W
3. Install the required libraries by copying them to the `lib` folder on the Pico W.
4. Open the `code.py` file in the MU Editor and run the code on the Pico W.

## Usage

1. Connect the Pico W to a computer using a USB cable.

2. Open a web browser and navigate to the IP address of the Pico W (e.g., `http://`).

3. Use the web interface to enter text that you want the Pico W to type out.

4. Watch as the Pico W types out the text after a 5-second delay.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have any suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
