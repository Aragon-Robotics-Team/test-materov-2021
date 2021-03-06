
"""
Configuration for everything
"""

from navigation1.Teleop import joy_init

class Config:
    def __init__(self):
        self.serialOn = True
        self.joyTestsOn = True
        self.deadBand = 0.07  # axis value must be greater than this number
        self.LH = 0  # Left horizontal axis
        self.LV = 1  # Left vertical axis
        self.RH = 2  # Right horizontal axis
        self.RV = 3  # Right vertical axis

        self.SpeedSize = 4
        self.MaxSpeed = 1900
        self.MinSpeed = 1100

        self.serialPort = '/dev/cu.usbmodem14401'
        self.minBytes = 10

        self.mapK = 400
        self.tspeedMiddle = 1500
        self.tspeedUp = 1700
        self.tspeedDown = 1300


        self.initSleep = 3
        self.loopSleep = 1/12

        self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, 0, 0, 0]  #this array keeps updating thruster values
        self.arduino = None
        self.j = None
    #
    # def joy_init(self):
    #     ######################## 1. Initializing Serial
    #     if self.serialOn:
    #         self.arduino = serial.Serial(port=self.serialPort, baudrate=115200, timeout=1)
    #     ######################## 2. Initializing PyGame
    #     pygame.init()  # Initiate the pygame functions
    #     pygame.joystick.init()
    #     pygame.display.init()
    #     self.j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    #     self.j.init()  # Initiate the joystick or controller
    #     controllerName = self.j.get_name()
    #     print('Detected controller : %s' % controllerName)
    #     print(pygame.joystick.get_count())
    #     # pygame.event.set_allowed(pygame.JOYBUTTONUP)
    #
    #     sleep(self.initSleep)
    #
    #     if controllerName == "Sony PLAYSTATION(R)3 Controller":
    #         joy_tests_ps3(self)
    #     else:
    #         joy_tests(self)
    #
    # def joy_tests_ps3(self):
    #     while self.joyTestsOn:
    #         sleep(0.1)
    #         for event in pygame.event.get():
    #             # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
    #             if event.type == pygame.JOYBUTTONDOWN:
    #                 if event.button == 0:
    #                     print("X Has Been Pressed")
    #                 if event.button == 1:
    #                     print("Circle has been pressed")
    #                 if event.button == 2:
    #                     print("Triangle has been pressed")
    #                 if event.button == 3:
    #                     print("Square has been pressed.")
    #                 if event.button == 4:
    #                     print("Shoulder L1 has been pressed")
    #                 if event.button == 5:
    #                     print("Shoulder R1 has been pressed")
    #                 if event.button == 6:
    #                     print("Surface Bottom Has Been Pressed")
    #                 if event.button == 7:
    #                     print("Shoulder R2 has been pressed")
    #                 if event.button == 8:
    #                     print("Share has been pressed")
    #                 if event.button == 9:
    #                     print("Start has been pressed. Will exit joytests")
    #                     LinearLoop(self)  # starts loop()
    #                 if event.button == 10:
    #                     print("Center has been pressed")
    #                     NonLinearLoop(self)
    #                 if event.button == 11:
    #                     print("Left Joystick button has been pressed")
    #                 if event.button == 12:
    #                     print("Right Joystick button Has Been Pressed")
    #                 if event.button == 13:
    #                     print("Surface up has been pressed")
    #                 if event.button == 14:
    #                     print("Surface bottom has been pressed")
    #                 if event.button == 15:
    #                     print("Surface left has been pressed")
    #                 if event.button == 16:
    #                     print("Surface Right has been pressed")
    #             elif event.type == pygame.JOYAXISMOTION:
    #                 if event.axis == 0 and abs(self.j.get_axis(0)) > self.deadBand:
    #                     zero = self.j.get_axis(0)
    #                     print('0 (left horizontal) has been moved ' + str(zero))
    #                 if event.axis == 1 and abs(self.j.get_axis(1)) > self.deadBand:
    #                     one = self.j.get_axis(1)
    #                     print('1 (left vertical) has been moved ' + str(one))
    #                 if event.axis == 2 and abs(self.j.get_axis(2)) > self.deadBand:
    #                     two = self.j.get_axis(2)
    #                     print('Shoulder L2 has been moved ' + str(two))
    #                 if event.axis == 3 and abs(self.j.get_axis(3)) > self.deadBand:
    #                     three = self.j.get_axis(3)
    #                     print('3 (right vertical) has been moved ' + str(three))
    #                 if event.axis == 4 and abs(self.j.get_axis(4)) > self.deadBand:
    #                     four = self.j.get_axis(4)
    #                     print('4 (right horizontal) has been moved ' + str(four))
    #
    # def joy_tests(self):
    #     while self.joyTestsOn:
    #         sleep(0.1)
    #         for event in pygame.event.get():
    #             # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
    #             if event.type == pygame.JOYBUTTONDOWN:
    #                 if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
    #                     print("Select Has Been Pressed")
    #                 if event.button == 1:
    #                     print("Left Joystick button has been pressed")
    #                 if event.button == 2:
    #                     print("Right Joystick button has been pressed")
    #                 if event.button == 3:
    #                     print("Start has been pressed. Will exit joytests.")
    #                     LinearLoop(self)
    #                 if event.button == 4:
    #                     print("Surface top button has been pressed")
    #                 if event.button == 5:
    #                     print("Surface right button has been pressed")
    #                 if event.button == 6:
    #                     print("Surface Bottom Has Been Pressed")
    #                 if event.button == 7:
    #                     print("Surface left button has been pressed")
    #                 if event.button == 8:
    #                     print("Left 2 has been pressed")
    #                 if event.button == 9:
    #                     print("Right 2 has been pressed")
    #                 if event.button == 10:
    #                     print("Left 1 has been pressed")
    #                 if event.button == 11:
    #                     print("Right 1 has been pressed")
    #                 if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
    #                     print("Triangle Has Been Pressed")
    #                 if event.button == 13:
    #                     print("Circle has been pressed")
    #                 if event.button == 14:
    #                     print("X has been pressed")
    #                 if event.button == 15:
    #                     print("Square has been pressed")
    #                 if event.button == 16:
    #                     print("Center PS has been pressed")
    #                     NonLinearLoop(self)
    #             elif event.type == pygame.JOYAXISMOTION:
    #                 if event.axis == 0 and abs(self.j.get_axis(0)) > self.deadBand:
    #                     zero = self.j.get_axis(0)
    #                     print('1 has been moved ' + str(zero))
    #                 if event.axis == 1 and abs(self.j.get_axis(1)) > self.deadBand:
    #                     one = self.j.get_axis(1)
    #                     print('2 has been moved ' + str(one))
    #                 if event.axis == 2 and abs(self.j.get_axis(2)) > self.deadBand:
    #                     two = self.j.get_axis(2)
    #                     print('3 has been moved ' + str(two))
    #                 if event.axis == 3 and abs(self.j.get_axis(3)) > self.deadBand:
    #                     three = self.j.get_axis(3)
    #                     print('4 has been moved ' + str(three))
    #                 if event.axis == 4 and abs(self.j.get_axis(4)) > self.deadBand:
    #                     four = self.j.get_axis(4)
    #                     print('x has been moved ' + str(four))
    #
    # def LinearLoop(self):
    #     program_starts = time()
    #     while True:
    #         pygame.event.pump()
    #
    #         """
    #         get buttons and thrusters
    #         calculations and edit tspeeds
    #         check if over or under boundary speeds
    #         set incoming arduino data array to tspeeds
    #         repeatedly check if teleop is being ended
    #         """
    #         buttonopen = self.j.get_button(self.squareButton)
    #         buttonclose = self.j.get_button(self.triangleButton)
    #         upconst = self.j.get_button(self.circleButton)
    #         downconst = self.j.get_button(self.xButton)
    #         JS_X = self.j.get_axis(self.LH)
    #         JS_Y = self.j.get_axis(self.LV)  # y-direction joystick values are flipped
    #         JS_Y_UD = self.j.get_axis(self.RV)
    #
    #         # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
    #         turn1, turn2, = JS_X * self.mapK, JS_X * self.mapK
    #         forward1, forward2 = JS_Y * self.mapK, JS_Y * self.mapK
    #         updown = JS_Y_UD * self.mapK
    #
    #         # calculating thruster speeds
    #         tspeeds = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, buttonopen,
    #                    buttonclose]
    #
    #         if abs(upconst) == 1:
    #             tspeeds[2] = self.tspeedUp  # 1700
    #             tspeeds[3] = self.tspeedUp
    #         elif abs(downconst) == 1:
    #             tspeeds[2] = self.tspeedDown  # 1300
    #             tspeeds[3] = self.tspeedDown
    #         elif abs(JS_Y_UD) > self.deadBand:
    #             tspeeds[2] = int(self.tspeedMiddle + updown)  # side thrusters
    #             tspeeds[3] = int(self.tspeedMiddle + updown)
    #
    #         if abs(JS_X) > self.deadBand and abs(JS_Y) > self.deadBand:
    #             tspeeds[0] = int(self.tspeedMiddle + forward1 + turn1)  # left thruster
    #             tspeeds[1] = int(self.tspeedMiddle + forward2 - turn2)  # right thruster
    #         elif abs(JS_X) > self.deadBand >= abs(JS_Y):  # only turn
    #             tspeeds[0] = int(self.tspeedMiddle + turn1)  # cast to integer
    #             tspeeds[1] = int(self.tspeedMiddle - turn2)
    #         elif abs(JS_X) <= self.deadBand < abs(JS_Y):
    #             tspeeds[0] = int(self.tspeedMiddle - forward1)  # cast to integer
    #             tspeeds[1] = int(self.tspeedMiddle - forward2)
    #
    #         # assign statuses
    #         self.arduinoParams = tspeeds
    #
    #         for i in range(self.SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
    #             self.arduinoParams[i] = min(self.MaxSpeed, self.arduinoParams[i])
    #             self.arduinoParams[i] = max(self.MinSpeed, self.arduinoParams[i])
    #
    #         if self.j.get_button(self.shareButton) == 1:
    #             serial_send_print(self)
    #             print("Stopping linear teleop")
    #             break
    #         serial_send_print(self)
    #         pygame.event.clear()
    #         time.sleep(self.loopSleep)
    #         now = time()
    #         print("It has been {0} seconds since the loop started".format(now - program_starts))
    #
    # def NonLinearLoop(self):
    #     while True:
    #         pygame.event.pump()
    #
    #         buttonopen = self.j.get_button(self.squareButton)
    #         buttonclose = self.j.get_button(self.triangleButton)
    #         upconst = self.j.get_button(self.circleButton)
    #         downconst = self.j.get_button(self.xButton)
    #         JS_X = self.j.get_axis(self.LH)
    #         JS_Y = self.j.get_axis(self.LV)  # y-direction joystick values are flipped
    #         JS_Y_UD = -self.j.get_axis(self.RV)
    #
    #         updown = JS_Y_UD * self.mapK
    #
    #         NL_X = self.mapK * (JS_X ** 3)
    #         NL_Y = self.mapK * (JS_Y ** 3)
    #
    #         tspeeds = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, buttonopen,
    #                    buttonclose]
    #
    #         # button z thrusters
    #         if abs(upconst) == 1:
    #             tspeeds[2] = self.tspeedUp
    #             tspeeds[3] = self.tspeedUp
    #         elif abs(downconst) == 1:
    #             tspeeds[2] = self.tspeedDown
    #             tspeeds[3] = self.tspeedDown
    #         elif abs(JS_Y_UD) > self.deadBand:
    #             tspeeds[2] = int(self.tspeedMiddle + updown)  # side thrusters
    #             tspeeds[3] = int(self.tspeedMiddle + updown)
    #
    #         if abs(JS_X) > self.deadBand and abs(JS_Y) > self.deadBand:  # calculate thruster values
    #             tspeeds[0] = int(self.tspeedMiddle + NL_X + NL_Y)
    #             tspeeds[1] = int(self.tspeedMiddle + (NL_X - NL_Y))
    #         elif abs(JS_X) > self.deadBand >= abs(JS_Y):  # only turn
    #             tspeeds[0] = int(self.tspeedMiddle + NL_X)  # cast to integer
    #             tspeeds[1] = int(self.tspeedMiddle - NL_X)
    #         elif abs(JS_X) <= self.deadBand < abs(JS_Y):  # only forward/back
    #             tspeeds[0] = int(self.tspeedMiddle - NL_Y)  # cast to integer
    #             tspeeds[1] = int(self.tspeedMiddle - NL_Y)
    #
    #         # assign statuses
    #         self.arduinoParams = tspeeds
    #
    #         for i in range(self.SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
    #             self.arduinoParams[i] = min(self.MaxSpeed, self.arduinoParams[i])
    #             self.arduinoParams[i] = max(self.MinSpeed, self.arduinoParams[i])
    #
    #         if self.j.get_button(self.shareButton) == 1:
    #             serial_send_print(self)
    #             print("Stopping Non-linear teleop")
    #             break
    #         serial_send_print(self)
    #         pygame.event.clear()
    #         sleep(self.loopSleep)
    #
    # def serial_send_print(self):  # print to terminal / send regularly updated array to arduino
    #
    #     stringToSend = ','.join(str(x) for x in self.arduinoParams) + '\n'
    #     print('py: ' + stringToSend)  # print python
    #     stringFromArd = ''
    #     if self.serialOn:
    #         self.arduino.write(stringToSend.encode("ascii"))  # send to arduino
    #         while self.arduino.in_waiting < self.minBytes:  # wait for data
    #             pass
    #         stringFromArd = self.arduino.readline().decode("ascii")  # read arduino data
    #     print('ard: ' + stringFromArd)  # print arduino data
    #
    #


class PS3Config(Config):
    def __init__(self):
        Config.__init__(self)
        # this is for the ps4 controller
        self.squareButton = 3  # button open
        self.triangleButton = 2  # button close
        self.circleButton = 1  # up constant speed
        self.xButton = 0  # down constant speed

        self.startButton = 9  # starts loop()
        self.shareButton = 8  # exits loop()

class PS4Config(Config):
    def __init__(self):
        Config.__init__(self)
        # this is for the ps3 controller
        self.squareButton = 15  # button open
        self.triangleButton = 12  # button close
        self.circleButton = 13  # up constant speed
        self.xButton = 14  # down constant speed

        self.startButton = 3  # starts loop()
        self.shareButton = 0  # exits loop()

if __name__ == "__main__":
    config = PS4Config()
    joy_init(config)
