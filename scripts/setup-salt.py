#!/usr/bin/python

# This script installs and configures the saltstack in the cloud datacenters.

import platform
import sys
import os

#########GLOBAL VARIABLES DECLERATION
dist=platform.linux_distribution()
#target = sys.argv[1]

#########FUNCTION DEFINATIONS
###
def usage():
	print "WTF. Use correct number of arguments"

def prep_up_the_host():		
	enable_epel()
	if dist[1] == "6.4":
		subscribe_redhat_server_options_channel()

def enable_epel():
	print "Installing EPEL package for your distribution"
	if dist[1] == "6.4":
		os.system("rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm")
	elif dist[1] == "5.4":
		os.system("rpm -Uvh http://epel.mirror.net.in/epel/5/i386/epel-release-5-4.noarch.rpm ")
	else:
		print "This is an unsupported platform version"
		exit(2)

def subscribe_redhat_server_options_channel():
	os.system("spacewalk-channel --user=corp-ood --password=4oneone --add --channel=rhel-x86_64-server-optional-6")	
	print "This host is now subscribed to below channel on Redhat" 
	os.system("spacewalk-channel --list")
	
def install_salt(target):
	if target == "master":
		os.system("yum install salt-master")
		os.system("chkconfig salt-master on")
	elif target == "minion":
		os.system("yum install salt-minion")
		os.system("chkconfig salt-minion on")



#########Main Body
###
print len(sys.argv)
if (len(sys.argv) < 2) | (len(sys.argv) > 4):
	usage()
	exit(1)
#else:
#	target = sys.argv[1]
	
print "Welcome to the SaltStack setup program"
print
print "This is a RHEL",dist[1], "host"
prep_up_the_host()
install_salt(target)
