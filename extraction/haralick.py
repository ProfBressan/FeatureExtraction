
# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - Haralick
dependencies : mahotas | numpy | PIL
References   :
    ----------
    HARALICK, Robert M.; SHANMUGAM, Karthikeyan; DINSTEIN, Its' Hak. Textural features
    for image classification. IEEE Transactions on systems, man, and cybernetics, n. 6, 
    p. 610-621, 1973.,

Using        : 
	from bic import Haralick
	haralick = Haralick() 
	featuresHaralick = haralick.extractionFeatures('img.jpg')
	print('Haralick --> ', featuresHaralick)
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
			img = Image.open(self.image_path).convert('RGB').convert('L')
			textures = mt.features.haralick(np.asanyarray(img))
			ht_mean = textures.mean(axis=0)
			return ht_mean
		except Exception as e:
			print('\n################# (haralick) - Error in processing!  #################\n', e)
