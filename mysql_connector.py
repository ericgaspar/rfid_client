#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, os, time, mysql.connector

rfiddb = mysql.connector.connect(host    = 'localhost',   	# Mettre l'adresse du server mysql
		      		user     = 'root', 		# Mettre le nom du client
			    	password = 'password',		# Mettre le mot de passe
	    			database = 'RFID_DB')		# Mettre le nom de la base de donnee
