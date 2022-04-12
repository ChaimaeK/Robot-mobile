## 01_SNT prog h_  nanoS
import board
import time
import pulseio
import busio
from adafruit_motor import servo

BTgreg = busio.UART(board.D10, board.D11, baudrate=9600)

MLI = pulseio.PWMOut(........., frequency=50)
mon_servo = servo.Servo(MLI, min_pulse=700, max_pulse=2300, actuation_range=140)
MLI1 = pulseio.PWMOut(........., frequency=50)
mon_servo2 = servo.Servo(MLI1, min_pulse=700, max_pulse=2300, actuation_range=140)

while True:
    time.sleep(0.1)
    data = BTgreg.read(1)
    if data is not None:
        donnees_recues = chr(data[0])  # on convertit le premier element en caractere
        print("j'ai recu la lettre", donnees_recues)      
        if donnees_recues == "z":
            mon_servo.angle = 30
            mon_servo2.angle = 104
            time.sleep(5)
            print("Avant")
        elif donnees_recues == "x":
            mon_servo.angle = 74
            mon_servo2.angle = 74
            time.sleep(1)
            mon_servo.angle = 104
            mon_servo2.angle = 30
            print("Arriere")
        elif donnees_recues == "q":
            mon_servo.angle = 74
            mon_servo2.angle = 74
            time.sleep(1)
            mon_servo.angle = 30
            mon_servo2.angle = 30
            time.sleep(1)
            mon_servo.angle = 74
            mon_servo2.angle = 74
            print("Gauche")
        elif donnees_recues == "d":
            mon_servo.angle = 74
            mon_servo2.angle = 74
            time.sleep(1)
            mon_servo.angle = 104
            mon_servo2.angle = 104
            time.sleep(1)
            mon_servo.angle = 74
            mon_servo2.angle = 74
            print("Droite")
        elif donnees_recues == "s":
            mon_servo.angle = 74
            mon_servo2.angle = 74
            print("Arret")
        else:
            print("ce n'est pas un ordre connu")
    