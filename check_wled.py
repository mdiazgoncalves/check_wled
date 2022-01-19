#!/usr/bin/python3

# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for your plugin
import argparse
import requests

# Return codes expected by Nagios
codes = ['OK', 'WARNING', 'CRITICAL', 'UNKNOWN']

# Create the parser
my_parser = argparse.ArgumentParser(description='Check WLED node availability and status')

# Add the arguments
my_parser.add_argument('hostname', metavar='<hostname>', type=str, help='The hostname/ip of the device')

# Execute the parse_args() method
args = my_parser.parse_args()

# Check logic starts here

try:
    response = requests.get('http://' + args.hostname + '/json')
    response.raise_for_status()
except requests.exceptions.RequestException  as e:
    STATUS = 2
    MESSAGE =str(e)
else:
    data = response.json()
    STATUS = 0
    MESSAGE = f"name:{data['info']['name']} on:{data['state']['on']} mac_address:{':'.join(data['info']['mac'][i:i+2] for i in range(0,12,2))} version:{data['info']['ver']}"

# Print the message for nagios
print(f"{codes[STATUS]} - {MESSAGE}")

# Exit with status code
raise SystemExit(STATUS)
