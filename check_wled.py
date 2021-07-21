#!/usr/bin/python3

# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for your plugin
import argparse
import requests

# Return codes expected by Nagios
codes = [ 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN' ]

# Create the parser
my_parser = argparse.ArgumentParser(description='Check WLED node availability')

# Add the arguments
my_parser.add_argument('hostname', metavar='<hostname>', type=str, help='The hostname/ip of the device')

# Execute the parse_args() method
args = my_parser.parse_args()

# Check logic starts here

try:
    response = requests.get('http://' + args.hostname + '/json')
    response.raise_for_status()
except requests.exceptions.RequestException  as e:
    status = 2
    message =str(e)
else:
    data = response.json()
    status = 0
    message = "name:{} on:{} mac_address:{} version:{}".format(data['info']['name'],data['state']['on'],':'.join(data['info']['mac'][i:i+2] for i in range(0,12,2)),data['info']['ver'])

# Print the message for nagios
print("{} - {}".format(codes[status], message))

# Exit with status code
raise SystemExit(status)
