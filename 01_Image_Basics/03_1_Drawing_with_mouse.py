######################
### SIMPLE CIRCLES ###
######################

import numpy as np
import cv2

### FUNCTION ###
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255, 0, 100), -1)

### BLACK IMAGE ###
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(winname='my_drawing')
# connect y=the button to callback function
cv2.setMouseCallback('my_drawing', draw_circle) # here use the function


while True:
    # Show the image window
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()