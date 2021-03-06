# Importing Libraries
import struct

import cv2
import pygame
import serial
import time
from time import sleep
from struct import *
from tkinter import *

arduino = None
j = None
serialOn = False
joyTestsOn = True

videoCaptureObject = cv2.VideoCapture(0)
result = True

# global in a function will be visible to the whole program
deadBand = 0.12  # axis value must be greater than this number
LH = 0  # Left horizontal axis
LV = 1  # Left vertical axis
RH = 2  # Right horizontal axis
RV = 3  # Right vertical axis

serialPort = '/dev/cu.usbmodem14101'
controllerName = None

top = Tk()

mapK = 400
tspeedMiddle = 1500

startButton = 9  # starts loop()
shareButton = 8  # exits loop()
squareButton = 3  # button open
triangleButton = 2  # button close

initSleep = 3
loopSleep = 1/5

toArduino = [tspeedMiddle, tspeedMiddle, 0, 0]  #this array keeps updating thruster values


def init():
    ######################## 1. Initializing Serial
    if serialOn:
        global arduino
        arduino = serial.Serial(port=serialPort, baudrate=115200, timeout=1)
    ######################## 2. Initializing PyGame
    pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init()
    global j
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller
    global controllerName
    controllerName = j.get_name()
    print('Detected controller : %s' % controllerName)
    # pygame.event.set_allowed(pygame.JOYBUTTONUP)

    sleep(initSleep)
    if controllerName == "Sony PLAYSTATION(R)3 Controller":
        joy_tests_ps3()
    elif controllerName == "Sony PLAYSTATION (R)4 Controller":
        joy_tests()


def joy_tests():
    while joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        print("X Has Been Pressed")
                    if event.button == 1:
                        print("Circle has been pressed")
                    if event.button == 2:
                        print("Triangle has been pressed")
                    if event.button == 3:
                        print("Square has been pressed.")
                    if event.button == 4:
                        print("Shoulder L1 has been pressed")
                    if event.button == 5:
                        print("Shoulder R1 has been pressed")
                    if event.button == 6:
                        print("Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print("Shoulder R2 has been pressed")
                    if event.button == 8:
                        print("Select has been pressed")
                    if event.button == 9:
                        print("Start has been pressed. Will exit joytests")
                        loop() # starts loop()
                    if event.button == 10:
                        print("Center has been pressed")
                    if event.button == 11:
                        print("Left Joystick button has been pressed")
                    if event.button == 12:
                        print("Right Joystick button Has Been Pressed")
                    if event.button == 13:
                        print("Surface up has been pressed")
                    if event.button == 14:
                        print("Surface bottom has been pressed")
                    if event.button == 15:
                        print("Surface left has been pressed")
                    if event.button == 16:
                        print("Surface Right has been pressed")
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(j.get_axis(0)) > deadBand:
                    zero = j.get_axis(0)
                    print('0 (left horizontal) has been moved ' + str(zero))
                if event.axis == 1 and abs(j.get_axis(1)) > deadBand:
                    one = j.get_axis(1)
                    print('1 (left vertical) has been moved ' + str(one))
                if event.axis == 2 and abs(j.get_axis(2)) > deadBand:
                    two = j.get_axis(2)
                    print('Shoulder L2 has been moved ' + str(two))
                if event.axis == 3 and abs(j.get_axis(3)) > deadBand:
                    three = j.get_axis(3)
                    print('3 (right vertical) has been moved ' + str(three))
                if event.axis == 4 and abs(j.get_axis(4)) > deadBand:
                    four = j.get_axis(4)
                    print('4 (right horizontal) has been moved ' + str(four))


def joy_tests_ps3():
    global startButton
    global shareButton
    global squareButton
    global triangleButton
    startButton = 3  # starts loop()
    selectButton = 0  # exits loop()
    squareButton = 15  # button open
    triangleButton = 12  # button close

    while joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                        print("Select Has Been Pressed")
                    if event.button == 1:
                        print("Left Joystick button has been pressed")
                    if event.button == 2:
                        print("Right Joystick button has been pressed")
                    if event.button == 3:
                        print("Start has been pressed. Will exit joytests.")
                        loop()
                    if event.button == 4:
                        print("Surface top button has been pressed")
                    if event.button == 5:
                        print("Surface right button has been pressed")
                    if event.button == 6:
                        print("Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print("Surface left button has been pressed")
                    if event.button == 8:
                        print("Left 2 has been pressed")
                    if event.button == 9:
                        print("Right 2 has been pressed")
                    if event.button == 10:
                        print("Left 1 has been pressed")
                    if event.button == 11:
                        print("Right 1 has been pressed")
                    if event.button == 12: # event.type == pygame.JOYBUTTONUP:
                        print("Triangle Has Been Pressed")
                    if event.button == 13:
                        print("Circle has been pressed")
                    if event.button == 14:
                        print("X has been pressed")
                    if event.button == 15:
                        print("Square has been pressed")
                    if event.button == 16:
                        print("Center PS has been pressed")
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(j.get_axis(0)) > deadBand:
                    zero = j.get_axis(0)
                    print('1 has been moved ' + str(zero))
                if event.axis == 1 and abs(j.get_axis(1)) > deadBand:
                    one = j.get_axis(1)
                    print('2 has been moved ' + str(one))
                if event.axis == 2 and abs(j.get_axis(2)) > deadBand:
                    two = j.get_axis(2)
                    print('3 has been moved ' + str(two))
                if event.axis == 3 and abs(j.get_axis(3)) > deadBand:
                    three = j.get_axis(3)
                    print('4 has been moved ' + str(three))
                if event.axis == 4 and abs(j.get_axis(4)) > deadBand:
                    four = j.get_axis(4)
                    print('4 has been moved ' + str(four))


def loop():
    while True:
        pygame.event.pump()
        #get buttons
        #get thrusters
        #write and read

        buttonopen = j.get_button(squareButton)
        buttonclose = j.get_button(triangleButton)
        JS_X = j.get_axis(LH)
        JS_Y = j.get_axis(LV) # y-direction joystick values are flipped

        # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
        turn1, turn2,  = JS_X * mapK, JS_X * mapK
        forward1, forward2 = JS_Y * mapK, JS_Y * mapK
        # calculating thruster speeds

        if abs(JS_X) > deadBand and abs(JS_Y) > deadBand:
            tspeed_1 = int(tspeedMiddle + forward1 + turn1)  # left thruster
            tspeed_2 = int(tspeedMiddle + forward2 - turn2)  # right thruster
        elif abs(JS_X) > deadBand >= abs(JS_Y):  # only turn
            tspeed_1 = int(tspeedMiddle + turn1)  # cast to integer
            tspeed_2 = int(tspeedMiddle - turn2)
        elif abs(JS_X) <= deadBand < abs(JS_Y):
            tspeed_1 = int(tspeedMiddle - forward1)  # cast to integer
            tspeed_2 = int(tspeedMiddle - forward2)
        else:
            tspeed_1 = 1500
            tspeed_2 = 1500

        # assign statuses to toArduino
        toArduino[0] = tspeed_1  # left thruster
        toArduino[1] = tspeed_2  # right thruster
        toArduino[2] = buttonopen
        toArduino[3] = buttonclose

        for i in range(2):  # making sure thruster values don't go above 1900 and below 1100
            if toArduino[i] > 1900:
                toArduino[i] = 1900
            if toArduino[i] < 1100:
                toArduino[i] = 1100

        if j.get_button(shareButton) == 1:
            serial_send_and_print(1500, 1500, 0, 0)
            break
        serial_send_and_print(str(toArduino[0]), str(toArduino[1]), str(toArduino[2]), str(toArduino[3]))
        pygame.event.clear()
        sleep(loopSleep)


def serial_send_and_print(w, x, y, z):

    stringToSend = str(w) + ',' + str(x) + ',' + str(y) + ',' + str(z) + '\n'
    print('py: ' + stringToSend)  # print python
    if serialOn:
        arduino.write(stringToSend.encode("ascii"))  # send to arduino
        while arduino.in_waiting < 10:  # wait for data
            pass
        data = arduino.readline().decode("ascii")  # read arduino data
        print('ard: ' + data)  # print arduino data
    else:
        print('ard: serial not on')

def guiinit():
    btn = Button(top, text = "hello", command = asdf)
    btn.pack()

    top.mainloop()

def asdf():
    print("hello")

def videoInit():
    while result:
        ret, frame = videoCaptureObject.read()
        cv2.imshow("Capturing Video", frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            videoCaptureObject.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    import multiprocessing as mp

    joystickprocess = mp.Process(target = init)
    guiprocess = mp.Process(target = guiinit)
    videoprocess = mp.Process(target = videoInit)
    joystickprocess.start()
    guiprocess.start()
    videoprocess.start()

