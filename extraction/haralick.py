
# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com / (43)99924-9391

Description  : Features Extraction - Haralick
dependencies : mahotas | OpenCV
References   :
    ----------
    HARALICK, Robert M.; SHANMUGAM, Karthikeyan; DINSTEIN, Its' Hak. Textural features
    for image classification. IEEE Transactions on systems, man, and cybernetics, n. 6, 
    p. 610-621, 1973.,
"""
 

import mahotas as mt
from PIL import Image
import numpy as np

class Haralick:
	def __init__(self):
		self.image_path = ''
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
			textures = mt.features.haralick(np.asanyarray(imgGray))
			ht_mean = textures.mean(axis=0)
			return ht_mean
		except Exception as e:
			print('\n################# (haralick) - Error Reading Image!  #################\n', e)
