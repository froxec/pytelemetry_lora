from pytelemetry import Pytelemetry
from pytelemetry.transports.serialtransport import SerialTransport

if __name__ == "__main__":
    transport = SerialTransport()
    tlm = Pytelemetry(transport, 1, 868)
    transport.connect({'port': '/dev/ttyUSB0', 'baudrate': 115200})

    tlm.publish('HALO', 2,  868, 8.0, 'float32')