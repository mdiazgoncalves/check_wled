#!/usr/bin/python3

# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for your plugin
import argparse
import requests
from requests.auth import HTTPBasicAuth

# Return codes expected by Nagios
codes = [ 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN' ]

# Create the parser
my_parser = argparse.ArgumentParser(description='Check WLED node availability')

# Add the arguments
my_parser.add_argument('hostname', metavar='<hostname>', type=str, help='The hostname/ip of the device')
my_parser.add_argument('-U', "--username", metavar='username', type=str, help='the WLED api username')
my_parser.add_argument('-P', "--password", metavar='password', type=str, help='the WLED api password')

# Execute the parse_args() method
args = my_parser.parse_args()

# Check logic starts here

try:
    response = requests.get('http://' + args.hostname + '/json/info', auth=HTTPBasicAuth(args.username, args.password))
    response.raise_for_status()
except requests.exceptions.RequestException  as e:
    status = 2
    message =str(e)
else:
    data = response.json()
    status = 0
    message = "name:{} mac_address:{} version:{}".format(data['name'],':'.join(data['mac'][i:i+2] for i in range(0,12,2)),data['ver'])

# Print the message for nagios
print("{} - {}".format(codes[status], message))

# Exit with status code
raise SystemExit(status)
