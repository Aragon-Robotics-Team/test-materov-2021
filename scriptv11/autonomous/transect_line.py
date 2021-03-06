import cv2
import numpy as np
from time import sleep
import math

horizontal = [-1, -1, -1, -1]
vertical = [ -1, -1, -1, -1]
numH = 0
numV = 0
posH = -1
posV = -1
center_width = 0
center_height = 0
width = 0
height = 0
transectRow = ["right", "left", "right"]
#sense whether or not there are no lines in the areas that are supposed to be empty to make sure that vertical doesn't change back prematurely
#Only switch if there is no line in the bottom half
rowCount = 0
mode = "hor"

def angleBetweenLines(x1, y1, x2, y2, x3, y3): #given 3 points, where x1,y1 is the shared point
    v1 = (x2-x1, y2-y1)
    v2 = (x3-x1, y3-y1)
    dot = np.dot(v1, v2)
    magv1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magv2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cosAngle = dot/(magv1*magv2)
    angle = math.acos(cosAngle) #in radians
    # print("x1: " + str(x1))
    # print("x2:" + str(x2))
    # print("x3: " + str(x3))
    # print(angle)
    return(angle)

def horOrVert(x1, x2, y1, y2):
    global horizontal
    global vertical
    global numH
    global numV
    if y2 <= y1:
        filler = y1
        y1 = y2
        y2 = filler
        filler = x1
        x1 = x2
        x2 = filler
    angle_radians = angleBetweenLines((int(center_width)), (int(height)), x2+(int(center_width))-x1, y2+(int(height))-y1, (int(center_width)), 0)
    angle = math.degrees(angle_radians)
    # print(angle)
    if (angle >= 90 and angle < 135):
        horizontal = [x1, y1, x2, y2] #the last horizontal line is saved
        # print("horizontal")
        numH = numH + 1
    if (angle >= 135 and angle < 181):
        # print("vertical")
        vertical = [x1, y1, x2, y2] #the last vertical line is saved
        numV = numV + 1

def findPosition():
    global numH
    global numV
    global horizontal
    global vertical
    global posH
    global posV
    global img

    if numH > 0:
        # print("Number of Horizontal Lines: " + str(numH))
        # print("Horizontal Line: " + str(horizontal))
        # print(horizontal)
        cv2.line(img, (horizontal[0], horizontal[1]), (horizontal[2], horizontal[3]), (100, 0, 0), 10) #draws one horizontal line
        posH = (horizontal[0] + horizontal[2])/2
        # print("Position: " + str(posH))
    if numV > 0:
        # print("Number of Vertical Lines: " + str(numV))
        # print("Vertical Line: " + str(vertical))
        cv2.line(img, (vertical[0], vertical[1]), (vertical[2], vertical[3]), (100, 0, 0), 10) #draws one vertical line
        posV = (vertical[0] + vertical[2])/2
        # print("Position: " + str(posV))

def sendToThrusters():
    global mode
    global rowCount
    global no_line
    global empty_frame_count
    if no_line == True:
        empty_frame_count = empty_frame_count + 1
        output = "none"
        if empty_frame_count == 10: #only stop running program if there has consistently been no line found
            output = "stop"
        return output
    else:
        empty_frame_count = 0
        if mode == "hor":
            if transectRow[rowCount] == "right":

                if posV < (center_width + 25) and posV >= (center_width - 25):
                    if (horizontal[0] < center_width  and horizontal[2] < center_width):
                        mode = "ver"
            elif transectRow[rowCount] == "left":
                #return thruster values to move left (thrusters move backwards)
                if posV < (center_width + 25) and posV >= (center_width - 25):
                    if (horizontal[0] > center_width and horizontal[2] > center_width):
                        mode = "ver"
        if mode == "ver":
            #return thruster values to move down
            if posH < (center_height + 25) and posH >= (center_height - 25):
                if (vertical[1] < center_height and vertical[3] < center_height): #Only change if the vertical line is not in the bottom half of the screen
                    mode = "hor"
                    rowCount = rowCount + 1

def findLines(image):
    global numH
    global numV
    global center_width
    global height
    global center_height
    global width
    global img
    global no_line

    img = image
    width = img.shape[1]
    center_width = width/2
    height = img.shape[0]
    center_height = height/2

    #change to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #mask everything but the red
    lower_red = np.array([0,50,50]) #example value
    upper_red = np.array([10,255,255]) #example value
    mask = cv2.inRange(gray_hsv, lower_red, upper_red)
    # mask = cv2.bitwise_and(img, img, mask=mask)

    #simplifies everything that is not masked to be red (should help lessen the lines in the actual thing?)
    img[mask>0]=(0,0,255)

    mask = cv2.bitwise_and(gray_hsv, gray_hsv, mask=mask)
    # cv2.imshow("asdf", img)
    # cv2.imshow("asdf", mask)

    #find lines
    # cv2.waitKey(0)

    edges = cv2.Canny(mask, 75, 150)


    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)

    #
    if lines is None:
        print("no lines")
        no_line = True
        #STOP THE THING?
    elif len(lines) > 0:
    # if len(lines) > 0:
    # if lines:
    # elif len(lines) > 0:
        no_line = False
        numH = 0 #resets the number of horizontal and vertical lines per frame
        numV = 0
        for line in lines:
           x1, y1, x2, y2 = line[0]
           # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
           horOrVert(x1, x2, y1, y2)
           findPosition()
           print("Mode: " + str(mode))
           print("Row count: " + str(rowCount))
           print("transectRow: " + str(transectRow[rowCount]))

           #detect angle between lines
    # else:
    #     print("no lines")

    #
    # imS = cv2.resize(img, (960, 540))


    # cv2.imshow("linesDetected", imS)
    # sleep(0.5)

    # cv2.waitKey(0)

    # cv2.destroyAllWindows()

def autoTransect(image):
    findLines(image)
    sendToThrusters()

if __name__ == "__main__":
    videoCaptureObject = cv2.VideoCapture(1)
    result = True

    sleep(1)
    print("start")
    while result:
        ret,frame = videoCaptureObject.read()
        # cv2.imshow("Capturing Video",frame)
        autoTransect(frame)
        cv2.imshow("linesDetected", img)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            videoCaptureObject.release()
            result = False
            cv2.destroyAllWindows()
