#insert import statements
import glob
import gui #use gui.top.update()

import cv2
from video_input import general_video
from video_input import photomosaic

from nav.controller import joy_init
from nav.controller import joytests
import threading

from img_proc import imgqueue

#joy_init() #for controllers

# t1 = threading.Thread(target=joytests) <-- doesn't work because pygame is not threadsafe
# t1.start()
#
# t1 = threading.Thread(target = video)
# t1.start()
#
# print("starting thruster process")
# multiprocessing.set_start_method('spawn')
# thruster_proc = multiprocessing.Process(target = thrusterProcess)
# auto_queue = multiprocessing.Queue()

if __name__ == "__main__":
    while True:
        #joytests() #<-- Fatal error sometimes?????
        #imgqueue.queue() #<-- same effect as directly calling the video module; it lags bc the images are being shown and the controller
        #is being checked at the same time
        gui.root.update()
        if glob.photomosaicVideo == True:
            photomosaic()
        # else:
        #     general_video()
        #video.general_video()


#MOVE TELEOP/SERIAL (WITH SLEEP) IN ONE PROCESS, EVEYRTHING ELSE IN ANOTHER PROCESS <-- ISOLATE SLEEP IN ONE PROCESS TO AVOID LAG
#In order to match up the two processes and avoid impedance mismatch. Only add event into the queue
#if the queue is empty, that way, only the events that the teleop/serial process can run at the time is added in, so there is no built up lag
#Use priority queue to make sure the new command in queue has priority
