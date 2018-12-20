## Setting up DDNS with Namecheap on Raspberry Pi

After the script (``ddns.py``) is saved in the home directory of ``pi`` user, change the permissions of the file so that it can be run directly.

```bash
$ cd ~
$ sudo chmod u+x ddns.py
$ ./ddns.py
```

Then edit the crontab file

```bash
$ crontab -e
```

and add the following lines to the end of the file

```
@reboot /home/pi/ddns.py
*/10 * * * * /home/pi/ddns.py
```

