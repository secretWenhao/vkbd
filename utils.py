import cv2
import sys
import numpy

def initCam():
	cam = cv2.VideoCapture(0)
	if not cam:
		sys.stdout.write("camInit() Error! Aborting.")
		sys.exit(1)
	return cam

def guideLines(img, hor=2, vert=2, color=(0,0,255)):
	H,W,D = img.shape
	for i in range(1, hor):
		start = (0, i * H / hor)
		stop = (W, i * H / hor)
		cv2.line(img, start, stop, color)
	for i in range(1, vert):
		start = (i * W / vert, 0)
		stop = (i * W / vert, W)
		cv2.line(img, start, stop, color)
	return img

def findKbd(cam):
	while cv2.waitKey(30) & 0xFF != ord('c'):
		ret, frame = cam.read()
		cv2.imshow("Image", guideLines(frame, 4, 4))