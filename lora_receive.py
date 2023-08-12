from pytelemetry import Pytelemetry
from pytelemetry.transports.serialtransport import SerialTransport
import time
import argparse
def callback(topic, data, opts):
    print("NO HALO!!")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--port')
    parser.add_argument('--lora_addr')
    parser.add_argument('--lora_freq', default=868)
    parser.add_argument('--baudrate', default=115200)
    args = parser.parse_args()

    transport = SerialTransport()
    tlm = Pytelemetry(transport, args.lora_addr, args.lora_freq)
    transport.connect({'port': args.port, 'baudrate': args.baudrate})

    tlm.subscribe('HALO', callback)


    while True:
        tlm.update()
        time.sleep(0.5)