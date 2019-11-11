
# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com / (43)99924-9391

Description  : Features Extraction - Surf
dependencies : mahotas | OpenCV
References   :
    ----------
    Herbert Bay, Andreas Ess, Tinne Tuytelaars, Luc Van Gool "SURF: Speeded Up
    Robust Features", Computer Vision and Image Understanding (CVIU), Vol. 110,
    No. 3, pp. 346--359, 2008
"""
from mahotas.features import surf
from PIL import Image
import numpy as np

class Surf:
	def __init__(self):
		self.image_path = ''
		self.p0 = 0.5
		self.p1 = 0.5
	def setImagePath(self, image_path):
		self.image_path = image_path
	def getImagePath(self):
		return self.image_path
	def extractionFeatures(self, image_path):
		try:
			self.image_path = image_path
			img = Image.open(self.image_path)
			imgRGB = img.convert('RGB')
			imgGray = imgRGB.convert('L')
			textures = surf.surf(np.asanyarray(imgGray))
			vFeatures = textures.mean(axis=0)
			return vFeatures
		except Exception as e:
			print('\n################# (Moments) - Error Reading Image!  #################\n', e ,'\n')
