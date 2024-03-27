import cv2 as cv
import mediapipe as mp 


class HandDetector():
	def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5) :
		self.mode = mode
		self.maxHands = maxHands
		self.detectionCon = detectionCon
		self.trackCon = trackCon
		self.mp_hands = mp.solutions.hands
		self.model = self.mp_hands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
		self.mp_draw = mp.solutions.drawing_utils

	def find_hands(self, image, draw_connections = False):
		self.image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		self.results = self.model.process(self.image_rgb)
		if self.results.multi_hand_landmarks:
			for handlms in self.results.multi_hand_landmarks:
				if draw_connections:
					self.mp_draw.draw_landmarks(image, handlms, self.mp_hands.HAND_CONNECTIONS)
				else :
					self.mp_draw.draw_landmarks(image, handlms)
		return image

	def find_position(self, image, hand_no = 0):
		lm_list = []
		if self.results.multi_hand_landmarks:
			target_hand = self.results.multi_hand_landmarks[hand_no]
			for id , lm in enumerate(target_hand.landmark):
				h , w , c = image.shape
				cx , cy = int(lm.x * w) , int(lm.y * h)
				cv.circle(image, (cx,cy), 15, (255,0,0), cv.FILLED)

if __name__ == "__main__" :

	detector = HandDetector()
	capture = cv.VideoCapture(0)

	while True :
		ret, frame = capture.read()
		frame = detector.find_hands(frame)
		detector.find_position(frame)
		cv.imshow("webcam", frame)
		if cv.waitKey(1) & 0xff == ord("q"):
			break

	capture.release()
	cv.destroyAllWindows()