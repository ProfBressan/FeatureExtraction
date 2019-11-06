
# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com 

Description  : Features Extraction - Zernike Moments
dependencies : mahotas | OpenCV
"""
import mahotas as mt
import cv2

class Zernike:
	def __init__(self):
		self.image_path = ''
		self.radius = 15
		self.degree = 8
	def setImagePath(self, image_path):
		self.image_path = image_path
	def getImagePath(self):
		return self.image_path
	def extractionFeatures(self, image_path):
		self.image_path = image_path
		try:
			image = cv2.imread(self.image_path)
			imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			Features = mt.features.zernike(imgGray,self.radius,self.degree)
			return Features
		except Exception as e:
			print('\n################# (Zernike) - Error Reading Image!  #################\n', e ,'\n')
