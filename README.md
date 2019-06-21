# uPyThings
Trying out some things with MicroPython


## Manage script 
* `python manage.py --port PORT flash_firmware`
    * Flashes MicroPython firmware (uses esptool)
    * Optional arg `-p PORT` or `--port PORT` for the port (default: dev)
    * Optional arg `-e` or `--erase` to erase flash
* `python manage.py --port PORT flash_scrips`
    * Uploads all scripts in the src directory (uses ampy)
    * Optional arg `-p PORT` or `--port PORT` for the port (default: dev)
* `python manage.py --port PORT monitor`
    * Monitor and REPL to esp (uses miniterm)
    * Optional arg `-p PORT` or `--port PORT` for the port (default: dev)
    * Optional arg `-b BAUD` or `--baud BAUD` to erase flash (default: 115200)
