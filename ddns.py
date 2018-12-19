#!/usr/bin/python3
from requests import get, codes


class ANSI:
    """
    This class contains the ANSI escape codes for printing to the console as
    well as commonly used combinations of these codes.
    """

    reset = "\033[0m"
    bold = "\033[1m"
    faint = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    blink = "\033[5m"
    inverse = "\033[7m"

    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        magenta = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"

        grey = "\033[90m"
        bright_red = "\033[91m"
        bright_green = "\033[92m"
        bright_yellow = "\033[93m"
        bright_blue = "\033[94m"
        bright_magenta = "\033[95m"
        bright_cyan = "\033[96m"
        bright_white = "\033[97m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        yellow = "\033[43m"
        blue = "\033[44m"
        magenta = "\033[45m"
        cyan = "\033[46m"
        white = "\033[47m"

        grey = "\033[100m"
        bright_red = "\033[101m"
        bright_green = "\033[102m"
        bright_yellow = "\033[103m"
        bright_blue = "\033[104m"
        bright_magenta = "\033[105m"
        bright_cyan = "\033[106m"
        bright_white = "\033[107m"

    @classmethod
    def OK(cls, content):
        return cls.fg.bright_green + cls.bold + content + cls.reset

    @classmethod
    def ERROR(cls, content):
        return cls.fg.bright_red + cls.bold + content + cls.reset


HOST = "@"
DOMAIN = "greenberg.io"
# Dynamic DNS password (NOT account)
PASSWORD = "PASSWORD"

print("Checking IP address... ", end="", flush=True)
ip_req = get(url='https://dynamicdns.park-your-domain.com/getip')
IP = ip_req.text
print(IP, flush=True)

print("Checking previous IP address... ", end="")
IP_CHANGED = True
filename = "ip.txt"
try:
    with open(filename, "r+") as f:
        prev_ip = f.read()
        print(prev_ip)

        if IP == prev_ip:
            IP_CHANGED = False

        f.seek(0)
        f.truncate()
        f.write(IP)

except FileNotFoundError:
    print("IP record file does not exist. Creating a new one.")
    with open(filename, "w") as f:
        f.write(IP)

if IP_CHANGED:
    print("IP address is new. Sending update to Namecheap DDNS.")

    ddns_url = "http://dynamicdns.park-your-domain.com/update?host={}&domain={}&password={}".format(
        HOST, DOMAIN, PASSWORD)
    update_req = get(ddns_url)

    print("Update request status: {} ".format(update_req.status_code), end="")
    if update_req.status_code == codes.ok:
        print(ANSI.OK("OK"))
    else:
        print(ANSI.ERROR("ERROR"))
else:
    print("IP address does not appear to have changed. No update sent.")
