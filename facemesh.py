import mediapipe as mp
import cv2 as cv
import numpy as np


capture = cv.VideoCapture(0)

mp_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils
draw_specs = mp_draw.DrawingSpec(thickness = 2, circle_radius = 1)
model = mp_face_mesh.FaceMesh(max_num_faces = 1)

while True:
    ret, frame = capture.read()
    # cv.imshow("webcam", frame_rgb)
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = model.process(frame_rgb)
    if results.multi_face_landmarks is not None:
        for face_lms in results.multi_face_landmarks:
            mp_draw.draw_landmarks(frame, face_lms, mp_face_mesh.FACE_CONNECTIONS, draw_specs)
    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xff == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
