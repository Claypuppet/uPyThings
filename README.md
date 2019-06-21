# uPyThings
Trying out some things with MicroPython


## Manage script 
* `python manage.py --port PORT flash_firmware`
    * Flashes MicroPython firmware (uses esptool)
    * Required arg `-p PORT` or `--port PORT` for the port
    * Optional arg `-e` or `--erase` to erase flash
* `python manage.py --port PORT flash_scrips`
    * Uploads all scripts in the src directory (uses ampy)
    * Required arg `-p PORT` or `--port PORT` for the port
* `python manage.py --port PORT monitor`
    * Monitor and REPL to esp (uses miniterm)
    * Required arg `-p PORT` or `--port PORT` for the port
    * Optional arg `-b BAUD` or `--baud BAUD` to erase flash (default 115200)
