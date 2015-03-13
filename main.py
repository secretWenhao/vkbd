from utils import initCam
import cv2

def main():
	cam = initCam()

	while (True):
		ret, frame = cam.read()
		cv2.imshow("Image", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cam.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()