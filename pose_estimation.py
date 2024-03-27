import mediapipe as mp
import cv2 as cv

mp_pose = mp.solutions.pose
model = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

capture = cv.VideoCapture("./video/poses.mp4")

while True:
    ret, frame = capture.read()
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = model.process(frame_rgb)
    mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv.imshow("video",frame)
    if cv.waitKey(1) & 0xff == ord("q"):
        break

capture.release()
cv.destroyAllWindows()