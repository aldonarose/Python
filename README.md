# handtracking
import cv2 as cv
import mediapipe as mp
import numpy as np

# creating the model.
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
model = mp_hands.Hands(maxHands = 4)  

img = cv.imread("../images/hand.jpg")


img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("hands",img_rgb)

results = model.process(img_rgb)
# print(results.multi_hand_landmarks)

for handlms in results.multi_hand_landmarks :
    mp_draw.draw_landmarks(img, handlms)
    
cv.imshow("hand",img)

cv.waitKey(0)
