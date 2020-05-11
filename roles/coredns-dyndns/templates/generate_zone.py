#!/usr/bin/python3

import os
import sys
import time

import jinja2

zonefile = sys.argv[1] + "/db.dyndns.zone"

v4_records = []
v6_records = []


template = jinja2.Template(
    open(
        os.path.dirname(
            os.path.abspath(__file__)) +
        '/zone_template.j2').read())

try:
    with open(zonefile, 'r') as file:
        old_content = file.read()
except FileNotFoundError:
    old_content = '\n\n\n\n'

for filename in os.listdir(sys.argv[1]):
    if filename.endswith(".dyndns"):
        with open(sys.argv[1] + "/" + filename, 'r') as file:
            v4 = file.readline()
            v6 = file.readline()
            if v4 != '\n':
                v4_records.append({
                    'domain': filename.replace(".dyndns", ''),
                    'address': v4
                })
            if v6 != '\n':
                v6_records.append({
                    'domain': filename.replace(".dyndns", ''),
                    'address': v6
                })

new_content = template.render(
    v4_records=v4_records,
    v6_records=v6_records,
    soa_serial=int(time.time()) - 1000000000)

new = '\n'.join(new_content.split('\n')[2:])
old = '\n'.join(old_content.split('\n')[2:])

if new != old:
    with open(zonefile, 'w') as file:
        file.write(new_content)
