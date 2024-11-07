# This script requires Flipper Zero with access to Sub-GHz functionality.
# Adjust frequency and other parameters as needed.

import time
import random

# Honeypot configuration
FREQUENCY = 433920000  # Example frequency in Hz for 433.92 MHz
RESPONSE_MESSAGE = "Go Fuck Yourselelf!"  # Message to send when signal is detected
REPEAT_COUNT = 1000  # Number of times to repeat response

# Function to transmit a message using Sub-GHz
def transmit_response():
    for _ in range(REPEAT_COUNT):
        # Send the response message "Go Fuck Yourself!"
        subghz.send_raw(RESPONSE_MESSAGE.encode(), FREQUENCY, modulation="ASK")
        time.sleep(0.01)  # Small delay to avoid overwhelming

# Function to listen for incoming signal on specified frequency
def listen_for_signal():
    while True:
        # Start listening on the specified frequency
        subghz.start_rx(FREQUENCY, timeout=5000)  # Timeout in milliseconds
        data = subghz.get_data()
        
        if data:
            # Log incoming data for analysis (replace with actual logging if possible)
            print(f"Signal detected: {data}")
            # Send repeated "hahaha" response
            print("Sending response...")
            transmit_response()
        
        time.sleep(1)  # Short delay before re-checking

# Main loop to start the honeypot
def main():
    print("Starting Flipper Zero honeypot...")
    listen_for_signal()

# Run the honeypot
main()
