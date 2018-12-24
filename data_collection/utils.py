import smtplib
from requests import get, codes
import json


def call_api(url):
    resp = get(url)
    if resp.status_code != codes['ok']:
        raise RuntimeError(
            "API Call Response returned error {} for URL: {}".format(resp.status_code, url))
    else:
        return json.loads(resp.text)


def send_email(message):
    fromaddr = 'siot@greenberg.io'
    toaddrs = ['bsg115@ic.ac.uk']

    msg = '''From: {fromaddr}\nTo: {toaddr}\nSubject: {subject}\n\n{body}\n'''

    subject = "SIOT Watchdog Alert"

    msg = msg.format(fromaddr=fromaddr,
                     toaddr=toaddrs[0], subject=subject, body=message)

    server = smtplib.SMTP('mx1.cc.ic.ac.uk:25')
    server.starttls()
    server.ehlo()
    server.sendmail(fromaddr, toaddrs[0], msg)
    print("Email sent")
    server.quit()


if __name__ == "__main__":
    text = "This is a test email from Python. You can discard it."
    send_email(text)
