from time import sleep
import time  
import RPi.GPIO as GPIO
import sys
import urllib2
from time import sleep
import math
import json
import threading

global counter

n_1=0;
n_2=0;
counter=0;


CHANNEL_ID = '644983'
readAPI = '46CQRK58CQ7WCS4F'
writeAPI = 'CJHLVAENFALG2AXC' 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % writeAPI 

initial_counter = 4;
n_1 = (initial_counter%10);
n_2 = (initial_counter/10);
counter = initial_counter;


conn = urllib2.urlopen(baseURL + '&field1=%s' % initial_counter)   #reset the counter
time.sleep(0.5)
conn.close()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

door1 = 25;           #inches
door2 = 45;

prevcounter=0;
timeout = 2;


update_second = 1;

#sensor1 is outside
#sensor2 is inside

A1 = 2;
B1 = 3;
C1 = 4;
D1 = 5;
E1 = 6;
F1 = 7;
G1 = 8;

A2 = 9;
B2 = 10;
C2 = 11;
D2 = 12;
E2 = 13;
F2 = 14;
G2 = 15;

sensor1 = 16;
sensor2 = 18;

GPIO.setup(A1, GPIO.OUT) #A
GPIO.setup(B1, GPIO.OUT) #B
GPIO.setup(C1, GPIO.OUT) #C
GPIO.setup(D1, GPIO.OUT) #D
GPIO.setup(E1, GPIO.OUT) #E
GPIO.setup(F1, GPIO.OUT) #F
GPIO.setup(G1, GPIO.OUT) #G

GPIO.setup(A2, GPIO.OUT) #A
GPIO.setup(B2, GPIO.OUT) #B
GPIO.setup(C2, GPIO.OUT) #C
GPIO.setup(D2, GPIO.OUT) #D
GPIO.setup(E2, GPIO.OUT) #E
GPIO.setup(F2, GPIO.OUT) #F
GPIO.setup(G2, GPIO.OUT) #G
 

def ONE_1():
    GPIO.output(A1, GPIO.HIGH)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.HIGH)
    GPIO.output(E1, GPIO.HIGH)
    GPIO.output(F1, GPIO.HIGH)
    GPIO.output(G1, GPIO.HIGH)
    return

def TWO_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.HIGH)
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(E1, GPIO.LOW)
    GPIO.output(F1, GPIO.HIGH)
    GPIO.output(G1, GPIO.LOW)
    return


def THREE_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(E1, GPIO.HIGH)
    GPIO.output(F1, GPIO.HIGH)
    GPIO.output(G1, GPIO.LOW)
    return

def FOUR_1():
    GPIO.output(A1, GPIO.HIGH)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.HIGH)
    GPIO.output(E1, GPIO.HIGH)
    GPIO.output(F1, GPIO.LOW)
    GPIO.output(G1, GPIO.LOW)
    return

def FIVE_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.HIGH)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(E1, GPIO.HIGH)
    GPIO.output(F1, GPIO.LOW)
    GPIO.output(G1, GPIO.LOW)
    return

def SIX_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.HIGH)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(E1, GPIO.LOW)
    GPIO.output(F1, GPIO.LOW)
    GPIO.output(G1, GPIO.LOW)
    return

def SEVEN_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.HIGH)
    GPIO.output(E1, GPIO.HIGH)
    GPIO.output(F1, GPIO.HIGH)
    GPIO.output(G1, GPIO.HIGH)
    return

def EIGHT_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(E1, GPIO.LOW)
    GPIO.output(F1, GPIO.LOW)
    GPIO.output(G1, GPIO.LOW)
    return

def NINE_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.HIGH)
    GPIO.output(E1, GPIO.HIGH)
    GPIO.output(F1, GPIO.LOW)
    GPIO.output(G1, GPIO.LOW)
    return

def ZERO_1():
    GPIO.output(A1, GPIO.LOW)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(C1, GPIO.LOW)
    GPIO.output(D1, GPIO.LOW)
    GPIO.output(E1, GPIO.LOW)
    GPIO.output(F1, GPIO.LOW)
    GPIO.output(G1, GPIO.HIGH)
    return

def ONE_2():
    GPIO.output(A2, GPIO.HIGH)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.HIGH)
    GPIO.output(E2, GPIO.HIGH)
    GPIO.output(F2, GPIO.HIGH)
    GPIO.output(G2, GPIO.HIGH)
    return

def TWO_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.HIGH)
    GPIO.output(D2, GPIO.LOW)
    GPIO.output(E2, GPIO.LOW)
    GPIO.output(F2, GPIO.HIGH)
    GPIO.output(G2, GPIO.LOW)
    return


def THREE_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.LOW)
    GPIO.output(E2, GPIO.HIGH)
    GPIO.output(F2, GPIO.HIGH)
    GPIO.output(G2, GPIO.LOW)
    return

def FOUR_2():
    GPIO.output(A2, GPIO.HIGH)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.HIGH)
    GPIO.output(E2, GPIO.HIGH)
    GPIO.output(F2, GPIO.LOW)
    GPIO.output(G2, GPIO.LOW)
    return

def FIVE_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.HIGH)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.LOW)
    GPIO.output(E2, GPIO.HIGH)
    GPIO.output(F2, GPIO.LOW)
    GPIO.output(G2, GPIO.LOW)
    return

def SIX_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.HIGH)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.LOW)
    GPIO.output(E2, GPIO.LOW)
    GPIO.output(F2, GPIO.LOW)
    GPIO.output(G2, GPIO.LOW)
    return

def SEVEN_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.HIGH)
    GPIO.output(E2, GPIO.HIGH)
    GPIO.output(F2, GPIO.HIGH)
    GPIO.output(G2, GPIO.HIGH)
    return

def EIGHT_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.LOW)
    GPIO.output(E2, GPIO.LOW)
    GPIO.output(F2, GPIO.LOW)
    GPIO.output(G2, GPIO.LOW)
    return

def NINE_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.HIGH)
    GPIO.output(E2, GPIO.HIGH)
    GPIO.output(F2, GPIO.LOW)
    GPIO.output(G2, GPIO.LOW)
    return

def ZERO_2():
    GPIO.output(A2, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(D2, GPIO.LOW)
    GPIO.output(E2, GPIO.LOW)
    GPIO.output(F2, GPIO.LOW)
    GPIO.output(G2, GPIO.HIGH)
    return


def distancereader(pin):
         
         time.sleep(0.002)
         GPIO.setup(pin, GPIO.OUT)   
         GPIO.output(pin, 0)  
         time.sleep(0.000002)  
         GPIO.output(pin, 1)  
         time.sleep(0.000005)  
         GPIO.output(pin, 0)  
         
         
         GPIO.setup(pin, GPIO.IN)
          
  
         while GPIO.input(pin)==0:  
            starttime=time.time()  
  
         while GPIO.input(pin)==1:  
            endtime=time.time()  
        
         duration=endtime-starttime  
         distance=(duration*34000/2)*(0.3937)
         
         time.sleep(0.002)
         GPIO.setup(pin, GPIO.OUT)   
         GPIO.output(pin, 0)
         time.sleep(0.002)
         
         return distance
         

         
def display1(n_1):
    
            
    if(n_1==1):
        ONE_1();

    elif(n_1==2):
        TWO_1();
        
    elif(n_1==3):
        THREE_1();        
       
    elif(n_1==4):
        FOUR_1();

    elif(n_1==5):
        FIVE_1();

    elif(n_1==6):
        SIX_1();
        
    elif(n_1==7):
        SEVEN_1();
        
    elif(n_1==8):
        EIGHT_1();
        
    elif(n_1==9):
        NINE_1();
        
    elif(n_1==0):
        ZERO_1();
        
    sleep(0.001);
    

def display2(n_2):
    
    
    if(n_2==1):
        ONE_2();

    elif(n_2==2):
        TWO_2();
        
    elif(n_2==3):
        THREE_2();        
       
    elif(n_2==4):
        FOUR_2();

    elif(n_2==5):
        FIVE_2();

    elif(n_2==6):
        SIX_2();
        
    elif(n_2==7):
        SEVEN_2();
        
    elif(n_2==8):
        EIGHT_2();
        
    elif(n_2==9):
        NINE_2();
        
    elif(n_2==0):
        ZERO_2();
        
    sleep(0.001);
    
def channel_val():
    
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,readAPI))

    response = TS.read()
    data=json.loads(response)

    b = data['field1']
    b = int(float(b))
        
    return b
  
display1(n_1);
display2(n_2);
    
def periodic_update():
    global counter
    evaluate = channel_val();
    while not (counter==evaluate):
        conn = urllib2.urlopen(baseURL + '&field1=%s' % counter)
        time.sleep(0.5)
        conn.close()
        time.sleep(0.1)
        evaluate = channel_val();
    threading.Timer(update_second, periodic_update).start()

periodic_update();
        
while(1):
    
    
        time.sleep(0.03)

        
        distance_1 = distancereader(sensor1);
        
        time.sleep(0.03)
        
        distance_2 = distancereader(sensor2);
        
        
        #decrementer
        
        
        if(distance_2<door2):
                            state2=1;
                            time_end = time.time() + timeout;
                                
                            while((state2==1) and (time.time() < time_end)):
                
                                             time.sleep(.1);
                                             distance_1 = distancereader(sensor1);
                                             
                                             if(distance_1<door1):
                                                                if(counter==0):
                                                                                counter = 0;
                                                                elif(counter>0):
                                                                                counter-=1;
                                                                freeze=1;
                    
                                                                while(freeze==1):
                            
                                                                                 time.sleep(.1);
                                                                                 distance_1 = distancereader(sensor1);
                            
                                                                                 if(distance_1>door1):
                                                                                                     freeze=0;
                                                                                                     time.sleep(.1);
                                                                                 else:
                                                                                      freeze=1;
                                                                state2=0;
                                             else:
                                                  state2=1;
        
        state1=0;
        state2=0; 
                    
         #incrementer
        
        if(distance_1<door1):
                            state1=1;
                            time_end = time.time() + timeout;
                            while((state1==1) and (time.time() < time_end)):
                
                                             time.sleep(.1);
                                             distance_2 = distancereader(sensor2);
                
                                             if(distance_2<door2):
                                                                counter+=1;
                                                                freeze=1;
                    
                                                                while(freeze==1):
                            
                                                                                 time.sleep(.1);
                                                                                 distance_2 = distancereader(sensor2);
                            
                                                                                 if(distance_2>door2):
                                                                                                     freeze=0;
                                                                                                     time.sleep(.1);
                                                                                 else:
                                                                                      freeze=1;
                                                                state1=0;
                                             else:
                                                  state1=1;
        
        state1=0;
        state2=0;
        
        if(counter==prevcounter):
            pass
                                 
        else:
             n_1 =  counter%10;
             n_2 =  counter/10;
             display1(n_1);
             display2(n_2);
             prevcounter = counter;
             
            
            
            
            
            
            
            
            
            
            
            
