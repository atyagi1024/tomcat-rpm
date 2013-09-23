#!/usr/bin/python

import re
import os
import pdb

def Get_rhn_username():
	xyz = []
	file_name = "/etc/sysconfig/rhn/systemid"
	fp1 = open(file_name, "r")

	match = re.compile(r'<name>username</name>')
	match1 = re.compile(r'<value><string>(.*)</string></value>')

	strings = re.findall(r'<value><string>(.*)</string></value>', fp1.read())

	return strings[0]


def Subscribe_redhat_server_options_channel():
        rhn_registered_username = Get_rhn_username()
	os.system("spacewalk-channel --user=%s --add --channel=rhel-x86_64-server-optional-6"%rhn_registered_username )
        print "This host is now subscribed to below channel on Redhat"
        os.system("spacewalk-channel --list")

def Register_the_host_to_RHN():
	print
	rhn_username = raw_input("Enter the RHN username: ")
	os.system("rhn_register")

def Is_registered(fname):
	return os.path.exists(fname)

#Register_the_host_to_RHN()

print Is_registered("/etc/sysconfig/rhn/systemid")
if not Is_registered("/etc/sysconfig/rhn/systemid"):
	print "iNot Registered"
else:
	print "Registered"

#Subscribe_redhat_server_options_channel()

