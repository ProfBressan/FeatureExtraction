# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - LBP (Local Binary Part)
Dependencies : mahotas |  PIL (Python Imaging Library) | numpy
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
	def __init__(self, radius = 2, n_points = 12 ):
		self.radius = radius
		self.n_points = n_points
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
			img = Image.open(self.image_path).convert('RGB').convert('L')
			arrayFeatures = lbp(np.asanyarray(img), self.radius, self.n_points)
			return arrayFeatures
		except Exception as e:
			print('\n################# (LBP) - Error in processing!  #################\n', e)