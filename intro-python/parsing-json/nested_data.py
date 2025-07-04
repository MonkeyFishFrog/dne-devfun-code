#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # Read in the JSON text
    json_text = file.read() 
    # TODO: Parse the contents of the JSON file into a variable
json_data = json.loads(json_text)

"""
{'ietf-interfaces:interface': {'description': 'Wide Area Network',
                               'enabled': True,
                               'ietf-ip:ipv4': {'address': [{'ip': '172.16.0.2',
                                                             'netmask': '255.255.255.0'}]},
                               'name': 'GigabitEthernet2'}}
"""


# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    print("{name}: {ip} {netmask}".format(
        name=interface["name"],
        ip=interface["ietf-ip:ipv4"]["address"][0]["ip"],
        netmask=interface["ietf-ip:ipv4"]["address"][0]["netmask"],
    ))
