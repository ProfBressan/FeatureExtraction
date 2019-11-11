
# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com / (43)99924-9391

Description  : Features Extraction - Zernike Moments
dependencies : mahotas | OpenCV
"""
import mahotas as mt
import numpy as np
from PIL import Image

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
			img = Image.open(self.image_path)
			imgRGB = img.convert('RGB')
			imgGray = imgRGB.convert('L')
			Features = mt.features.zernike(np.asanyarray(imgGray),self.radius,self.degree)
			return Features
		except Exception as e:
			print('\n################# (Zernike) - Error Reading Image!  #################\n', e ,'\n')
