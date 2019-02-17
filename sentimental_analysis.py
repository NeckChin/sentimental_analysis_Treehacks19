#imports
import cognitive_face as CF
import numpy
import pandas
import time
import datetime
import cv2
import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
CONSTANTS
TINTERVAL = 1
KEY = 'ecbdb7db95d440b09e1457215ecd547f'  # Replace with a valid Subscription Key here.

#setup
os.chdir("/home/neckchin/Treehacks2019")
CF.Key.set(KEY)

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

list1 = []

#definitions
def take_pic():
	camera_port = 0
	camera = cv2.VideoCapture(camera_port)
	time.sleep(0.1)  # If you don't wait, the image will be dark
	return_value, image = camera.read()
	cv2.imwrite("opencv.png", image)
	camera.release

def face_detect(img_url):
	global list1
	try:
		start_time = datetime.datetime.utcnow()
		result = CF.face.detect(img_url, True, False, "emotion")
		result = result[0].get('faceAttributes', {}).get('emotion')
		result = numpy.array([val for (key,val) in result.iteritems()])
		row = numpy.array(datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))
		row = numpy.append(row, result)
		list1.append(row)
	except IndexError:
		list1.append([datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'), -1, -1, -1, -1, -1, -1, -1, -1] )

#main
while True:
	take_pic()
	face_detect("opencv.png")
	time.sleep(TINTERVAL)
	os.remove("opencv.png")
	df = pandas.DataFrame(list1, columns = ['time', 'sadness', 'neutral', 'contempt', 'disgust', 'anger', 'surprise', 'fear', 'happiness'])
