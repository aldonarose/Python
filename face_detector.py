import cv2 as cv


img = cv.imread("./images/face2.jpg")


gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier("./haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 6)
print(faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

cv.imshow("img",img)
cv.waitKey(0)

