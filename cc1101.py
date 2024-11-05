import spidev
import time
import logging

# Logging setup to track connection attempts
logging.basicConfig(filename='honeypot_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

class CC1101Honeypot:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)  # SPI bus (0, 0) for Raspberry Pi
        self.spi.max_speed_hz = 500000  # SPI speed
        self.setup_transceiver()

    def setup_transceiver(self):
        # Configure the CC1101 transceiver to desired settings (frequency, data rate, etc.)
        self.write_register(0x00, 0x07)  # Example settings, change as needed

    def write_register(self, address, value):
        self.spi.xfer2([address, value])

    def read_register(self, address):
        response = self.spi.xfer2([address | 0x80, 0x00])
        return response[1]

    def check_for_data(self):
        # Check for incoming data by reading a CC1101 status register or buffer
        rssi = self.read_register(0x34)  # Example: RSSI register
        if rssi > threshold_value:  # Set threshold based on environment testing
            return True
        return False

    def read_data(self):
        # Reading data from the RX FIFO buffer
        buffer = []
        while True:
            byte = self.read_register(0x3F)  # Example RX FIFO register
            if byte == 0:  # Stop reading at end of message
                break
            buffer.append(chr(byte))
        return ''.join(buffer)

    def send_response(self, message, repeat=100):
        # Send "hahaha" repeatedly as a response
        for _ in range(repeat):
            for char in message:
                self.spi.xfer2([ord(char)])  # Send each character as byte
            time.sleep(0.01)  # Short delay between messages

    def listen_for_connection(self):
        # Continuously listen for connection attempts
        while True:
            if self.check_for_data():  # Detect incoming data
                data = self.read_data()
                logging.info(f"Connection attempt detected. Data: {data}")
                print("Connection detected. Sending response...")
                self.send_response("Go Fuck Yourself")
            time.sleep(1)  # Polling interval

# Main function to run the honeypot
def main():
    honeypot = CC1101Honeypot()
    honeypot.listen_for_connection()

if __name__ == "__main__":
    main()
