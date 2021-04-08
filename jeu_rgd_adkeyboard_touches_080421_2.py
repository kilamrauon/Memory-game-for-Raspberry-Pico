import machine
import utime
import random
from machine import Pin, PWM
from time import sleep


analog_value = machine.ADC(28)


sequence = []
niveau=0
#bool encore
i=0
aff=0
num=0
pin0 = machine.Pin(0, machine.Pin.OUT)
pin1 = machine.Pin(1, machine.Pin.OUT)
pin2 = machine.Pin(2, machine.Pin.OUT)
pin3 = machine.Pin(3, machine.Pin.OUT)
pin4 = machine.Pin(4, machine.Pin.OUT)
pin5 = machine.Pin(5, machine.Pin.OUT)
pin6 = machine.Pin(6, machine.Pin.OUT)
pin7 = machine.Pin(7, machine.Pin.OUT)
on_led = machine.Pin(25)
pwm_green = PWM(Pin(18))
pwm_blue = PWM(Pin(19))
pwm_red = PWM(Pin(20))
pwm_green.freq(1000)
pwm_red.freq(1000)
pwm_blue.freq(1000)
pin0.on()
pin1.on()
pin2.on()
pin3.on()
pin4.on()
pin5.on()
pin6.on()
pin7.on()
en_jeu = 1

# sequence correcte - tout clignote en vert
def ok():
    print ("ok")
    
    #sequence erronée - fin du jeu - tout clignote en rouge
        
def ko():
    print ("ko")
        
    # appui sur les touche et retour de 1 2 3 ou fin    
def touches():
    touche = 0
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    
    utime.sleep(0.2)
   # j = 0
   # j = int(reading/1000)
    
    while (touche == 0 ):
        j=0
        reading = analog_value.read_u16()
        j = int(reading/1000)
        
        if  j == 65:
            touche = 0
        elif j == 0:
            print ("bouton 1")
            touche = 1
            affichage(1)
    
        elif j == 9:
            print ("bouton 2")
            touche = 5
    
        elif j == 19:
            print ("bouton 3")
            touche = 5
        
        elif j == 31:
            print ("bouton 4")
            touche = 2
            affichage(2)
        
        elif j == 47:
            print ("bouton 5")
            touche = 3
            affichage(3)
            
   
   
   # pwm_red.duty_u16(reading)
    sleep(0.01)
    
    return touche
    
    # a
def affiche_sequence():
    print("affiche sequence")
    
def feu_tricolore(duree):
    pin0.off()
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.on()
    pin5.on()
    pin6.on()
    pin7.on()
    on_led.toggle()
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(255*255)
    pwm_blue.duty_u16(255*255)
   
    sleep(duree)
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(127*255)
    pwm_blue.duty_u16(255*255)
   
    sleep(duree)
    pwm_red.duty_u16(255*255)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(255*255)
   
    sleep(duree)
    
def affichage(aff):
    eteint_led()
    if aff == 1 :
        print("1")
        pwm_red.duty_u16(0)
        pwm_green.duty_u16(255*255)
        pwm_blue.duty_u16(255*255)
        pin2.off()
        pin3.off()
        
        
    if aff == 2:
        print("2")
        pwm_red.duty_u16(255*255)
        pwm_green.duty_u16(0)
        pwm_blue.duty_u16(255*255)
        pin4.off()
        pin5.off()
        
    if aff == 3 :
        print("3")
        pwm_red.duty_u16(255*255)
        pwm_green.duty_u16(255*255)
        pwm_blue.duty_u16(0)
        pin6.off()
        pin7.off()
    
    sleep(0.5)
    eteint_led()
        
def eteint_led():
    pin0.on()
    pin1.on()
    pin2.on()
    pin3.on()
    pin4.on()
    pin5.on()
    pin6.on()
    pin7.on()
    sleep(0.1)
    
def allume_led():
    pin0.off()
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    pin5.off()
    pin6.off()
    pin7.off()
    
def clignote(couleur,duree):
    eteint_led()
    #allume_led()
    k=0
    for k in (0,6):
        sleep(duree)
        allume_led()
        if (couleur=="rouge"):
            pwm_red.duty_u16(0)
            pwm_green.duty_u16(255*255)
            pwm_blue.duty_u16(255*255)
        if (couleur=="vert"):    
            pwm_red.duty_u16(255*255)
            pwm_green.duty_u16(0)
            pwm_blue.duty_u16(255*255)
        if (couleur=="bleu"):    
            pwm_red.duty_u16(255*255)
            pwm_green.duty_u16(255*255)
            pwm_blue.duty_u16(0)
        
        sleep(duree)
        eteint_led()
        #sleep(duree)
    eteint_led()
        
while True:
    
    ##juste les 2 premières led alluméesok
    #top depart
  
    #feu_tricolore(.1)
    
   
    
    feu_tricolore(1)
    # sequence correcte - tout clignote en vert
    sequence = []
    en_jeu=1
    niveau = 0
    while (en_jeu == 1):
        num = random.randint(1, 3)
        sequence.append(num)
        clignote("vert",0.5)
        for i in range (0, niveau+1):
            # ajout d'un élément à sequence
            #print ("niveau", i)
            if sequence[i] == 1:
                affichage(1)
              
            elif sequence[i] == 2:
                affichage(2)
               
            elif sequence[i] == 3:
                affichage(3)
                
                #sleep(0.5)
        print("sequence finie")
                
        
        #au tour du joueur
        clignote("bleu",0.5)
       # sleep(1)
        
        for i in range(0,niveau+1):
            resultat = touches()
            print ("touche=",resultat)
            #resultat = sequence[i]
            if (resultat == sequence[i]):
                en_jeu=1
                touche = 0
                ok()
            else:
                en_jeu=0
                clignote("rouge",1)
                ko()
                break
            sleep(0.5)
        
        
        niveau = niveau + 1
        print("niveau+",niveau)
        