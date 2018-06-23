import os
import threading

def drowsinessDetect():
	os.system("sudo modprobe bcm2835-v4l2")
	os.system("python ~/IOT/Drowsiness\ detection/donotsleep.py --shape-predictor ~/IOT/Drowsiness\ detection/landmarks.dat --alarm ~/IOT/Drowsiness\ detection/alarm.wav")

def navigation():
	os.system("waze")

t1 = threading.Thread(target=drowsinessDetect, args=[])
t2 = threading.Thread(target=navigation, args=[])

t1.start()
t2.start()
