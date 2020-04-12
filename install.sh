#!/bin/bash

########################################################################
# rfid client for Raspberry Zero                                       #
# 3/06/2019                                                            #
########################################################################

if [ "$(whoami)" != "root" ]; then
	echo "Run script as ROOT ! (sudo bash install.sh)"
	exit
fi

echo "------------------------------------------------------------------"
echo " RFID CLIENT installation"
echo "------------------------------------------------------------------"

# Solve locales Perl language issue
export LANGUAGE=fr_FR.UTF-8
export LANG=fr_FR.UTF-8
export LC_ALL=fr_FR.UTF-8
locale-gen fr_FR.UTF-8
dpkg-reconfigure locales

# Update de Raspberry Pi
apt-get update -y && apt-get upgrade -y
apt-get install -y git vim python3-pip acl
pip3 install mysql.connector

apt-get autoremove -y
apt-get autoclean -y

#activate SPI and reboot
raspi-config
