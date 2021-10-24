# importing OpenCV library
import cv2
# importing MediaPipe library and naming it mp
import mediapipe as mp
# importing time library
import time

# MediaPipe solution drawing uitls
mp_drawing = mp.solutions.drawing_utils
# MediaPipe solution drawing styles
mp_drawing_styles = mp.solutions.drawing_styles
# MediaPipe Hands
mp_hands = mp.solutions.hands

""" MediaPipe Hands processes an RGB image and returns
    the hand landmarks and handedness of each detected
    hand.
"""
# capturing video from webcam
cap = cv2.VideoCapture(0)

# with statement helps in file and exception handling
with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:
    # while video is being captured
    while cap.isOpened():
        # reading frame and storing condition in success and frame in image
        success, image = cap.read()
        print(image)
        

# # keep capturing the frames
# while True:
#     # success = if frame is captured or not, img = frame
#     success, img = cap.read()

#     # calculating frame rate
#     # current time
#     cTime = time.time()
#     # frame rate
#     fps = int(1 / (cTime - pTime))
#     # update previous time
#     pTime = cTime

#     # show frame rate
#     cv2.putText(img, str(fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

#     # display frame
#     cv2.imshow("Frame", img)
#     # showing frame for atleast 1ms
#     cv2.waitKey(1)