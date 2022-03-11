import cv2

videoCaptureObject = cv2.VideoCapture(-1)
result = True

while result:
    ret,frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video",frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()