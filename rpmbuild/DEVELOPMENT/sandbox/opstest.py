#!/usr/bin/python

import yaml
import socket
import termcolor
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nodegroup', help='Checks connectivity to target server/cluster. nodegroup could be db,ftps,ldap, xops. If your argumnet is double letter e.g. cloud manager, you would need to use that between double or single quotes. Complete list of nodegroups that can be passed as arguments can be found in rules.yaml')
args = parser.parse_args()

f = open('rules.yaml')
datamap = yaml.safe_load(f)
f.close()

def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
	s.connect((ip, int(port)))
	s.shutdown(2)
    	return True
    except:
	return False

def Check_connectivity(key):
	try:
		target = datamap[key]['target']
		print termcolor.colored('Checking connectivity for ','magenta') +key
		print
		for port in datamap[key]['ports']:
        		if isOpen(target,port):
                		print "Connectivity test for port " +str(port) +"\t..............................." +termcolor.colored('SUCCESS','green')
		        else:
        		        print "Connectivity test for port " +str(port) +"\t..............................." +termcolor.colored('FAIL','red','on_yellow')
		print
	except KeyError:
		print "Invalid Argument"


if args.nodegroup == 'all':
	for key in datamap.keys():
		Check_connectivity(key)
	exit(0)
else:
	Check_connectivity(args.nodegroup)
