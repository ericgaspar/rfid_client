#!/bin/bash

####################################################################################
#	rfid client for Raspberry Zero                                             #
#	4/5/2019                                                                   #
####################################################################################


if [ "$(whoami)" != "root" ]; then
	echo "Run script as ROOT ! (sudo bash install.sh)"
	exit
fi

# Define user Domain Name
echo "------------------------------------------------------------------------------"
echo " NGinx + PHP7-FPM + MySQL installation"
echo "------------------------------------------------------------------------------"
echo

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

apt-get install -y rpi-update

apt-get install -y git vim acl


apt-get autoremove -y
apt-get autoclean -y

# Summary
echo
echo "------------------------------------------------------------------------------"
echo "               NGinx + PHP7-FPM + MySQL installation finished"
echo "------------------------------------------------------------------------------"
echo " NGinx configuration folder:       /etc/nginx"
echo " NGinx default site configuration: /etc/nginx/sites-enabled/default"
echo " NGinx default HTML root:          /var/www/$DOMAIN"
echo
echo " HTML page:                        `hostname -I`"
echo " To acces phpMyAdmin:              $DOMAIN/phpmyadmin"
echo " User:                             root"
echo " Password:                         $mysqlPass"
echo "------------------------------------------------------------------------------"
echo

read -p "Do you want to start raspi-config? <y/N> " prompt
if [ "$prompt" = "y" ]; then
	raspi-config
else
	echo "------------------------------------------------------------------------------"
	echo "                         Installation finished"
	echo "------------------------------------------------------------------------------"
fi
