import time
import RPi.GPIO as GPIO
import math
import xbox
import os 
# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#Rear Left Wheel
BENA  = 36
BINT1 = 38
BINT2 = 40
GPIO.setup(BENA, GPIO.OUT) 
GPIO.setup(BINT1, GPIO.OUT) 
GPIO.setup(BINT2, GPIO.OUT)
p1=GPIO.PWM(36,100)

#Rear Right Wheel
BENB  = 11 
BINT3 = 13
BINT4 = 15
GPIO.setup(BENB, GPIO.OUT) 
GPIO.setup(BINT3, GPIO.OUT) 
GPIO.setup(BINT4, GPIO.OUT)
p2=GPIO.PWM(11,100)

#Front Left Wheel
ENA  = 33
INT1 = 35
INT2 = 37
GPIO.setup(ENA, GPIO.OUT) 
GPIO.setup(INT1, GPIO.OUT) 
GPIO.setup(INT2, GPIO.OUT)
p3=GPIO.PWM(33,100)

#Front Right Wheel
ENB  = 19 
INT3 = 21
INT4 = 23
GPIO.setup(ENB, GPIO.OUT) 
GPIO.setup(INT3, GPIO.OUT) 
GPIO.setup(INT4, GPIO.OUT)
p4=GPIO.PWM(19,100)

#Add for safe shutdown
Shutoff  = 22
GPIO.setup(Shutoff, GPIO.IN)
input =GPIO.input(22)


if __name__ == '__main__':
    joy = xbox.Joystick()
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    
    while not joy.Back():
        spd = abs(joy.leftY() * 100)
        direction = abs(joy.leftX()*100)
        Math = math.sqrt(spd*spd + direction*direction)
        if Math >100:
            Math =100
        
        #print("speed = ",spd,"direction = ", direction)
        if joy.leftY() > 0:
            GPIO.output(BINT2, GPIO.HIGH)#set to low when complete
            GPIO.output(BINT3, GPIO.HIGH)
            GPIO.output(INT1, GPIO.HIGH)
            GPIO.output(INT4, GPIO.HIGH)
            
            if joy.leftX() ==0:
                p1.ChangeDutyCycle(spd)
                p2.ChangeDutyCycle(spd)
                p3.ChangeDutyCycle(spd)
                p4.ChangeDutyCycle(spd)           
            if joy.leftX() <0:
                p1.ChangeDutyCycle(spd)
                p2.ChangeDutyCycle(Math)
                p3.ChangeDutyCycle(spd)
                p4.ChangeDutyCycle(Math)
            if joy.leftX() >0:
                p1.ChangeDutyCycle(Math)
                p2.ChangeDutyCycle(spd)
                p3.ChangeDutyCycle(Math)
                p4.ChangeDutyCycle(spd)

            
        else:    
            GPIO.output(BINT2, GPIO.LOW)#set to low when complete
            GPIO.output(BINT3, GPIO.LOW)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT4, GPIO.LOW)
            
        if joy.leftY() < 0:
            GPIO.output(BINT1, GPIO.HIGH)#set to low when complete
            GPIO.output(BINT4, GPIO.HIGH)
            GPIO.output(INT2, GPIO.HIGH)
            GPIO.output(INT3, GPIO.HIGH)
            
            if joy.leftX() ==0:
                p1.ChangeDutyCycle(spd)
                p2.ChangeDutyCycle(spd)
                p3.ChangeDutyCycle(spd)
                p4.ChangeDutyCycle(spd)           
            if joy.leftX() <0:
                p1.ChangeDutyCycle(spd)
                p2.ChangeDutyCycle(Math)
                p3.ChangeDutyCycle(spd)
                p4.ChangeDutyCycle(Math)
            if joy.leftX() >0:
                p1.ChangeDutyCycle(Math)
                p2.ChangeDutyCycle(spd)
                p3.ChangeDutyCycle(Math)
                p4.ChangeDutyCycle(spd)            
        else:    
            GPIO.output(BINT1, GPIO.LOW)#set to low when complete
            GPIO.output(BINT4, GPIO.LOW)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT3, GPIO.LOW)
            
        if joy.leftY() ==0 and joy.leftX()>0:
            GPIO.output(BINT4, GPIO.HIGH)
            GPIO.output(INT1, GPIO.HIGH)
            GPIO.output(INT3, GPIO.HIGH)
            GPIO.output(BINT2, GPIO.HIGH)
            p1.ChangeDutyCycle(Math)
            p2.ChangeDutyCycle(Math)
            p3.ChangeDutyCycle(Math)
            p4.ChangeDutyCycle(Math)
            
        else:
            GPIO.output(BINT4, GPIO.LOW)
            GPIO.output(INT1, GPIO.LOW)
            GPIO.output(INT3, GPIO.LOW)
            GPIO.output(BINT2, GPIO.LOW)
            
        if joy.leftY() ==0 and joy.leftX()<0:
            GPIO.output(BINT3, GPIO.HIGH)
            GPIO.output(INT2, GPIO.HIGH)
            GPIO.output(INT4, GPIO.HIGH)
            GPIO.output(BINT1, GPIO.HIGH)
            p1.ChangeDutyCycle(Math)
            p2.ChangeDutyCycle(Math)
            p3.ChangeDutyCycle(Math)
            p4.ChangeDutyCycle(Math)
            
        else:
            GPIO.output(BINT3, GPIO.LOW)
            GPIO.output(INT2, GPIO.LOW)
            GPIO.output(INT4, GPIO.LOW)
            GPIO.output(BINT1, GPIO.LOW)
        

            

GPIO.cleanup()
joy.close()
