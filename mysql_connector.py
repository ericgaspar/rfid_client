#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, os, time, mysql.connector



rfiddb = mysql.connector.connect(host    = 'localhost',   	# Mettre l'adresse du server mysql (192.168.0.38)
		      		user     = 'root', 		# Mettre le nom du client (pi)
			    	password = 'password',		# Mettre le mot de passe (raspberry)
	    			database = 'rfid_data')	# Mettre le nom de la base de donnee (meteo_data)
