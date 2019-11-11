# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com 

Description  : Features Extraction - LBP (Local Binary Part)
Dependencies : mahotas | OpenCV
Configuration: radius = 2 | n_points = 12 --> features = 352
References   :
    ----------
        Gray Scale and Rotation Invariant Texture Classification with Local Binary Patterns
        Ojala, T. Pietikainen, M. Maenpaa, T. Lecture Notes in Computer Science (Springer)
        2000, ISSU 1842, pages 404-420

Using        : 
	from lbp import LBP
	lbp = LBP()
	featuresLBP = lbp.extractionFeatures('img.jpg')
	print('LBP --> ', featuresLBP)
"""
from mahotas.features import lbp
from PIL import Image
import numpy as np

class LBP:
	def __init__(self):
		# settings for LBP
		self.radius = 2
		self.n_points = 12
		self.image_path = ""
	def setRadius(self, radius):
		if (radius>0 and radius<5):
			self.radius = radius
	def getRadius(self):
		return self.radius
	def setNpoints(self, n_points):
		if (n_points>7 and n_points<13):
			self.n_points = n_points
	def getNpoints(self):
		return self.n_points
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
			arrayFeatures = lbp(np.asanyarray(imgGray), self.radius, self.n_points)
			return arrayFeatures
		except Exception as e:
			print('\n################# (LBP) - Error Reading Image!  #################\n', e)