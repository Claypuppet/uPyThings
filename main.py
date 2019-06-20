import machine
import time


def toggle(pin: machine.Pin) -> None:
    pin.value(not pin.value())


def main():
    pin_r = machine.Pin(1, machine.Pin.OUT)
    pin_g = machine.Pin(2, machine.Pin.OUT)
    pin_b = machine.Pin(3, machine.Pin.OUT)
    while 1:
        toggle(pin_r)
        time.sleep(0.5)
        toggle(pin_g)
        time.sleep(0.5)
        toggle(pin_b)
        time.sleep(0.3)


if __name__ == '__main__':
    main()
