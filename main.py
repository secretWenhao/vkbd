from utils import initCam
import cv2
from time import time
import sys

def main():
	cam = initCam()

	frames = 0
	startTime = time()

	while (True):
		ret, frame = cam.read()
		cv2.imshow("Image", frame)
		frames += 1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	stopTime = time()
	sys.stdout.write("Frames: %d\n" % frames)
	sys.stdout.write("Time: %0.4f sec.\n" % (stopTime - startTime))
	sys.stdout.write("Frame time: %0.04f\n" % ((stopTime - startTime)/frames))
	sys.stdout.write("FPS: %0.04f\n" % (frames/(stopTime - startTime)))
	# When everything done, release the capture
	cam.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()