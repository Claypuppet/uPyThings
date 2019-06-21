from machine import Pin, UART
import time
from external_libs.micropyGPS import MicropyGPS

uart = UART(2, 9600)

# queue / circular buffer
pin_g = Pin(2, Pin.OUT)
cp5s = [0 for i in range(0, 12)]

count = 0
current = 0


def button_pressed(p: Pin) -> None:
    global count
    count += 1
    pin_g.on()
    pin_g.off()


def toggle(pin: Pin) -> None:
    pin.value(not pin.value())


def loop_read_geiger():
    print("Initiating Geiger")
    global count, current
    pin_irover = Pin(4, Pin.IN)
    pin_irover.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)
    while 1:
        time.sleep(5)
        cp5s[current] = count
        count = 0
        print("cp5s", cp5s[current], "cpm", sum(cp5s))
        current = (current + 1) % 12


def loop_read_gps():
    print("Initiating GPS")
    uart.init(9600, bits=8, parity=None, stop=1)
    command = b'$PMTK220,5000*1B\r\n'  # Configure the GPS module to send every 5 seconds
    print(uart.write(bytearray(command)))

    my_gps = MicropyGPS()
    while 1:
        gps_bytes = uart.readline()
        if gps_bytes:
            for x in str(gps_bytes):
                my_gps.update(x)
            print(my_gps.latitude)


def main():
    time.sleep(1)
    # loop_read_geiger()
    loop_read_gps()


if __name__ == '__main__':
    main()

