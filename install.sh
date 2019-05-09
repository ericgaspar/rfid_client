#!/bin/bash

####################################################################################
#	rfid client for Raspberry Zero                                             #
#	9/5/2019                                                                   #
####################################################################################


if [ "$(whoami)" != "root" ]; then
	echo "Run script as ROOT ! (sudo bash install.sh)"
	exit
fi

echo "------------------------------------------------------------------------------"
echo " RFID installation"
echo "------------------------------------------------------------------------------"

# Solve locales Perl language issue
export LANGUAGE=fr_FR.UTF-8
export LANG=fr_FR.UTF-8
export LC_ALL=fr_FR.UTF-8
locale-gen fr_FR.UTF-8
dpkg-reconfigure locales

# Update de Raspberry Pi
apt-get update -y
apt-get upgrade -y
apt-get dist-upgrade -y
rpi-update -y
apt-get install -y git vim python3-pip acl
pip3 install mysql.connector

apt-get autoremove -y
apt-get autoclean -y

echo "------------------------------------------------------------------------------"
echo "                         Installation finished"
echo "------------------------------------------------------------------------------"

reboot
