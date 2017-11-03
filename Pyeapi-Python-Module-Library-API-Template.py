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

# get the instance of the API (in this case vlans)
vlans = node.api('vlans')

# return all vlans from the node
vlans.getall()

# return a specific vlan from the node
vlans.get(1)

# add a new vlan to the node
vlans.create(100)

# set the new vlan name
vlans.set_name(100, 'foo')
