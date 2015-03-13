import cv2
import sys

def initCam():
	cam = cv2.VideoCapture(0)
	if not cam:
		sys.stdout("camInit() Error! Aborting.")
		sys.exit(1)
	return cam