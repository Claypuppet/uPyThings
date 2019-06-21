"""
Just a hacky script to help with the some commands
"""

import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        metavar='command',
        type=str,
        choices=('upload_firmware', 'upload_scripts', 'monitor'),
        help='Command to execute'
    )
    parser.add_argument(
        '-p', '--port',
        type=str,
        dest='port',
        help='Device location, e.g. /dev/ttyUSBx or COMx',
        default='dev'
    )
    parser.add_argument(
        '-b', '--baud',
        dest='baud',
        type=str,
        help='Baudrate (default 115200)',
        default=115200
    )
    parser.add_argument(
        '-e', '--erase',
        dest='erase',
        action='store_const',
        const=True,
        default=False,
        help='Erase flash before upload firmware',
    )

    args = parser.parse_args()

    port = args.port
    baud = args.baud

    if not os.path.exists(port):
        print("PORT [%s] not found" % port)
        return 1

    if args.command == "upload_firmware":
        if args.erase:
            os.system('esptool.py --port %s erase_flash' % (port, ))
        os.system('esptool.py --chip esp32 --port %s --baud 460800 write_flash -z 0x1000 upy_firmware/esp32-20190620-v1.11-49-g34c04d231.bin' % (port, ))
        return
    if args.command == "upload_scripts":
        for filename in os.listdir('src'):
            print('uploading %s...' % filename)
            os.system('ampy --port %s put src/%s %s' % (port, filename, filename))
        return
    if args.command == "monitor":
        os.system('miniterm.py %s %s' % (port, baud))
        return


if __name__ == '__main__':
    main()
