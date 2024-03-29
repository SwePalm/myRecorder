#setting things up
import cv2
import numpy as np
import datetime as datetime

#i have created a simple framecounter, my camera does not support this prop
frameCounter = 0

# start working with the camera, using default TBD add camera number as arg
cap = cv2.VideoCapture(0)

#collecting some information and to be save in a csv file
logfile = np.array([["Frame Number","Timestamp"]])

while(True):
    #get frame-by-frame
    ret, frame = cap.read()

    #set-up frame counter
    frameCounter += 1

    #let add some information to the frame
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    frameNumber = str(frameCounter)
    displayText = timestamp + '  ' + frameNumber
    cv2.putText(frame,displayText,(130,30), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,255),2,cv2.LINE_AA)
  
    #Display the frame
    cv2.imshow('Camera feed', frame)

    #save info to logfile
    logfile = np.append(logfile, [[frameNumber,timestamp]], axis=0)

    #give the user an option to do something, q for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        np.savetxt('%s.csv' % timestamp, logfile, delimiter=',', fmt='%s')

        break

# Clean up as we are leaving
cap.release()
cv2.destroyAllWindows()
