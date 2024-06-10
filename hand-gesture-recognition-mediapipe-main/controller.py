import pyfirmata as py

print("Start")
port = "COM3"
board = py.ArduinoMega(port, baudrate=9600)

ENA=board.get_pin('d:11:o')
Rpin1 = board.get_pin('d:6:o')
Rpin2 = board.get_pin('d:7:o')
Lpin3 = board.get_pin('d:8:o')
Lpin4 = board.get_pin('d:9:o')
ENB=board.get_pin('d:12:o')
print("Connected")

speed=1
def RCCAR(msg):
    if msg=="Up":
        Rpin1.write(0)
        ENA.write(1)
        Rpin2.write(1)
        Lpin3.write(0)
        ENB.write(1)
        Lpin4.write(1)
        print("FORWARD")
        
        
    if msg=="Down":
        ENA.write(1)
        Rpin1.write(1)
        Rpin2.write(0)
        ENB.write(1)
        Lpin3.write(1)
        Lpin4.write(0)
        print("BACKWARD")

    if msg=="Left":
        Rpin1.write(0)
        Rpin2.write(1)
        Lpin3.write(1)
        Lpin4.write(0)
        print("LEFT")

    if msg=="Stop":
        Rpin1.write(0)
        Rpin2.write(0)
        Lpin3.write(0)
        Lpin4.write(0)
        print("BRAKE")

        
    if msg=="Right":
        Rpin1.write(1)
        Rpin2.write(0)
        Lpin3.write(0)
        Lpin4.write(1)
        print("RIGHT")
    

