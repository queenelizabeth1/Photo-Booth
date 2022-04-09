import numpy as np
import cv2
cap = cv2.VideoCapture(0)
n = 0

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))

    height = int(cap.get(4))

    smallFrame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
    img = np.zeros(frame.shape, np.uint8)
    img[:height, :width] = frame

    img[:height//2, :width//2] = smallFrame
    img[:height//2, width//2:] = smallFrame
    img[height//2:, width//2:] = smallFrame
    img[height//2:, :width//2] = smallFrame

    cv2.imshow('Photo Booth',img)
    
    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord('c'):
        cv2.imwrite('image' + str(n) + '.png',frame)
        n += 1

cap.release()
cv2.destroyAllWindows()
