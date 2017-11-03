#!/usr/local/bin/python

# Importing necessary modules
import sys
import json
import os
import pyeapi

# Create a node object by specifying the node to work with
pyeapi.load_config('nodes.conf')

# Create a connection to the node
node = pyeapi.connect_to('switch name from nodes.conf file')

# Send one or more commands to the node
output = node.enable('show hostname')
print(outout)

output = node.enable(['show hostname', 'show version'])
print(output)

# Send one or more configuration commands to the node
node.config('hostname veos01')

node.config(['interface Ethernet1', 'description foo'])



