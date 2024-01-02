#!/usr/bin/python3

# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for your plugin
import argparse
import requests

# Return codes expected by Nagios
CODES = ['OK', 'WARNING', 'CRITICAL', 'UNKNOWN']

# Create the parser
my_parser = argparse.ArgumentParser(description='Check WLED node availability and status')

# Add the arguments
my_parser.add_argument('hostname', metavar='<hostname>', type=str, help='The hostname/ip of the device')

# Execute the parse_args() method
args = my_parser.parse_args()


# Check logic starts here
def main():
    """
    Check availability and status
    """

    try:
        response = requests.get('http://' + args.hostname + '/json', timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as exception:
        status = 2
        message = str(exception)
    else:
        data = response.json()
        status = 0
        message = f"name:{data['info']['name']} on:{data['state']['on']} mac_address:{':'.join(data['info']['mac'][i:i+2] for i in range(0,12,2))} version:{data['info']['ver']}"

    # Print the message for nagios
    print(f"{CODES[status]} - {message}")

    # Exit with status code
    raise SystemExit(status)


if __name__ == "__main__":
    main()
