import cv2

img = cv2.imread('/Users/magdalenablum-oeste/Google Drive/GitHubMBO/OpenCV_Base/Blooms.jpg')

while True:
    cv2.imshow('Flowers', img)
    
    # If we have waited at least 1 ms and we have passed the Esc (has number 27)
     # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()