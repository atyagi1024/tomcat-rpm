#!/usr/bin/python
#
# This script does the basic install and configuration of the saltstack master and minions.
#Please feel free to modify this as per your requirement or report bugs/enhancement request to Atul Tyagi<atyagi@opsource.net>
#

import platform
import sys
import os

# FUNCTION DEFINATIONS

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
	
def show_usage():
    print
    print "Usage:",sys.argv[0],"  [options]"
    print
    print "Options:"
    print " master\t\t\tInstalls salt-master on the host."
    print " minion\t\t\tInstalls salt-minion on the host."
    print " -h, --help\t\tshow this help message and exit"
    print
    exit(1)

# Commandline parameter validation

def validate_commandline():
    number_of_parameters = len(sys.argv)
    if number_of_parameters > 2:
        print "Incorrect number of parameters. Please read the usage."
        show_usage()
    elif number_of_parameters == 1:
        show_usage()
    elif (sys.argv[1] != "master") & (sys.argv[1] != "minion") & (sys.argv[1] != "-h") & (sys.argv[1] != "--help"):
	print
        print sys.argv[0],": error: no such option: ",sys.argv[1]
        show_usage()
    elif (sys.argv[1] == "-h") | (sys.argv[1] == "--help") | (not sys.argv[1]):
        show_usage()
    elif sys.argv[1] == "master":
        target = "master"
    else:
        target = "minion"
    return target

dist=platform.linux_distribution()
target = validate_commandline()

# Main Body
print
print "******Welcome to the SaltStack setup program******"
print
print "This is a RHEL",dist[1], "host and as requested we are going to install and configure Salt",sys.argv[1]
print
choice = raw_input("Do you wish to continue...(y/N): ")
print "choice....", choice
if choice == 'N':
	print "Exiting the setup program. Thank you for using me."
	exit(3)
elif (choice == 'y') | (choice == 'Y')| ( not choice):
	prep_up_the_host()
	if (sys.argv[1] == "master"):
		target = "master"
	elif (sys.argv[1] == "minion"):
		target = "minion"
	install_salt(target)


"""
Documentation
=============

Known Bugs
===========
BZ1 - Update the RHEL versions in enable_epel()
BZ2 - Remove the RHN password while using spacewalk-channel under subscribe_redhat_server_options_channel()
BZ3 - subscribe_redhat_server_options_channel() should parse the system file to find the username for RHN registration.

Future Enhancements
===================
EN1 - Add support for accepting the master IP address in command line for minion configuration.
EN2 - Consolidate the usage() and usage_error() functions.......................................................................Completed
EN3 - Better validation of command line parameters..............................................................................Completed


### Change log
Fri Sep 13 11:50:48 EDT 2013:
	Initial script completed.
	Fixed enhancements EN2 and EN3
"""
