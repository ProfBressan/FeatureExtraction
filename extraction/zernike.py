
# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - Zernike Moments
dependencies : mahotas | numpy | PIL
References   :
    ----------
    Teague, MR. (1980). Image Analysis via the General Theory of Moments.  
	J. Opt. Soc. Am. 70(8):920-930.

Using        : 
	from zernike import Zernike
	zernike = Zernike() 
	featuresZernike = zernike.extractionFeatures('img.jpg')
	print('Zernike --> ', featuresZernike)
"""
import mahotas as mt
import numpy as np
from PIL import Image

class Zernike:
	def __init__(self, radius = 15, degree = 8):
		self.image_path = ''
		self.radius = radius
		self.degree = degree
	def setImagePath(self, image_path):
		self.image_path = image_path
	def getImagePath(self):
		return self.image_path
	def extractionFeatures(self, image_path):
		self.image_path = image_path
		try:
			img = Image.open(self.image_path).convert('RGB').convert('L')
			Features = mt.features.zernike(np.asanyarray(img),self.radius,self.degree)
			return Features
		except Exception as e:
			print('\n################# (Zernike) - Error in processing!  #################\n', e ,'\n')
