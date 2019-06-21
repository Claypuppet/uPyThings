import machine
import time
import libs.micropyGPS

# queue / circular buffer
pin_g = machine.Pin(2, machine.Pin.OUT)
cp5s = [0 for i in range(0, 12)]

count = 0


def button_pressed(p: machine.Pin) -> None:
    global count
    count += 1
    pin_g.on()
    pin_g.off()


def toggle(pin: machine.Pin) -> None:
    pin.value(not pin.value())


def main():
    global count
    current = 0
    pin_irover = machine.Pin(4, machine.Pin.IN)
    pin_irover.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed)
    while 1:
        time.sleep(5)
        cp5s[current] = count
        count = 0
        print("cp5s", cp5s[current], "cpm", sum(cp5s))
        current = (current + 1) % 12


if __name__ == '__main__':
    main()

