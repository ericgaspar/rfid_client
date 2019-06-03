#!/usr/bin/env python
# -*- coding: utf8 -*-

# Version modifiee de la librairie https://github.com/mxgxw/MFRC522-python

import RPi.GPIO as GPIO
import MFRC522
import signal
import mysql.connector
from mysql.connector import Error
from time import *
import time

db = mysql.connector.connect(
        host="ipduserver",
        user="nomduuser",
	    password="motdepasse",
	    database="nomdelabase")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

continue_reading = True

# Fonction qui arrete la lecture proprement 
def end_read(signal,frame):
    global continue_reading
    print ("Lecture terminée")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the Raspberry Pi RFID Login System"
print "Passer le tag RFID a lire"
print "Presser Ctrl-C pour quitter."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Detecter les tags
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

 # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        uid = str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])
        print uid

        # Light a LED for 1 second
    	GPIO.output(18,GPIO.HIGH)
    	sleep(1)
    	GPIO.output(18,GPIO.LOW)

        sleep(1)

        cur = db.cursor()
          
        # Read time and date
        currentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

        # Insert every login into database
        try:
            try:
                cur.execute("""INSERT INTO log_uid (id, uid, date) VALUES (%s, %s, %s)""",('NULL', uid, currentTime))
                db.commit()
            except Error as e :
                print(e)
        finally:
            print "Succes!"
            cur.close()

# This is the default key for authentication
key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

# Select the scanned tag
MIFAREReader.MFRC522_SelectTag(uid)

# Authenticate
status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

# Check if authenticated
if status == MIFAREReader.MI_OK:
    MIFAREReader.MFRC522_Read(8)
    MIFAREReader.MFRC522_StopCrypto1()
else:
    pass

db.close()