######################
### MOUSE MOVEMENT ###
######################

import numpy as np
import cv2

### FUNCTION ###
drawing = False # True if mause is pressed
ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
         if drawing == True:
                cv2.rectangle(img,(ix,iy), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
            
        
### BLACK IMG ###
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(winname='my_drawing')
# Connects the mouse button to the callback function
cv2.setMouseCallback('my_drawing', draw_circle)

### RUN FUNCTION ###
while True:
    cv2.imshow('my_drawing', img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    
cv2.destroyAllWindows()