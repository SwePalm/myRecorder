#setting things up
import cv2
import numpy as np
import datetime as datetime

# start working with the camera, using default TBD add camera number as arg

cap = cv2.VideoCapture(0)

while(True):
    #get frame-by-frame
    ret, frame = cap.read()

    #Display the frame
    cv2.imshow('Camera feed', frame)

    #give the user an option to do something, q for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up as we are leaving
cap.release()
cv2.destroyAllWindows()
