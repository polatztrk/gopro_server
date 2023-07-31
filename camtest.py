import numpy as np
import cv2
from datetime import datetime

cap1 = cv2.VideoCapture('rtmp://192.168.181.230:1936')
cap2 = cv2.VideoCapture('rtmp://192.168.181.230:1935')


frame_width1=int(cap1.get(3))
frame_height1=int(cap1.get(4))
frame_width2=int(cap2.get(3))
frame_height2=int(cap2.get(4))

size1=(frame_width1,frame_height1)
size2=(frame_width2,frame_height2)

dateObj=datetime.now()
result1=cv2.VideoWriter(f"{dateObj}-camera1.avi",cv2.VideoWriter_fourcc(*'MJPG'),120,size1)
result2=cv2.VideoWriter(f"{dateObj}-camera2.avi",cv2.VideoWriter_fourcc(*'MJPG'),120,size2)
while(True):
    # Capture frame-by-frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    result1.write(frame1)
    result2.write(frame2)
    resize1= cv2.resize(frame1,(700,400))
    resize2= cv2.resize(frame2,(700,400))
    
    final=cv2.hconcat([resize1,resize2])
    # Display the resulting frame
    #cv2.imshow('cam 1',frame1)
    #cv2.imshow('cam 2',frame2)
    cv2.imshow("Cam1&Cam2",final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cap2.release()
result1.release()
result2.release()
cv2.destroyAllWindows()
