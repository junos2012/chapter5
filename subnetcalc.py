#work with version 3 of python

import ipaddress
net = ipaddress.ip_network('192.168.0.0/26')
for a in net:
	print a
raw_input('Press enter to exit')