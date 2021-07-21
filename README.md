# check_WLED


Nagios plugin to check availability and the status of [WLED](https://kno.wled.ge/) devices. Checks if the WLED device is online and if its on or off.

## Installation

The installation requires Python 3.

I usually install additional plugins under `/usr/local/nagios/libexec`.

```
mkdir -p /usr/local/nagios/libexec
cd /usr/local/nagios/libexec
wget https://raw.githubusercontent.com/mdiazgoncalves/check_wled/main/check_wled.py
chmod +x check_wled.py
```

The [requests](https://github.com/psf/requests) module is required.

To install Requests, simply run this simple command in your terminal of choice:

```
python -m pip install requests
```

## Parameters

```
usage: check_wled.py [-h] <hostname>

Check WLED node availability and status

positional arguments:
  <hostname>            The hostname/ip of the device

```

## Support

Feel free to submit any issues and PRs.

## License

The project is licensed under GPL license. Happy monitoring.
