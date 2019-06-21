from machine import Pin, UART
import time
import libs.micropyGPS

uart = UART(1, 9600)

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
    uart.init(9600, bits=8, parity=None, stop=1)
    while 1:
        gps_string = uart.readline()
        if gps_string:
            print(gps_string)
        time.sleep(1)


def main():
    # loop_read_geiger()
    loop_read_gps()


if __name__ == '__main__':
    main()

