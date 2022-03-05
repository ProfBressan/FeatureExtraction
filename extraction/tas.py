
# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - TAS -  Threshold Adjacency Statistics
dependencies : mahotas, PIL (Python Imaging Library), numpy
References   :
    ----------
    COELHO, Luís Pedro et al. Structured literature image finder: extracting 
    information from text and images in biomedical literature. In: Linking 
    Literature, Information, and Knowledge for Biology. Springer, Berlin, 
    Heidelberg, 2010. p. 23-32.
Using        : 
	from tas import TAS
	tas = TAS() 
	featuresTAS = tas.extractionFeatures('img.jpg')
	print('TAS --> ', featuresTAS)
"""
from mahotas.features import tas
from PIL import Image
import numpy as np

class TAS:
	def __init__(self):
		self.image_path = ''
	def setImagePath(self, image_path):
		self.image_path = image_path
	def getImagePath(self):
		return self.image_path
	def extractionFeatures(self, image_path):
		try:
			self.image_path = image_path
			img = Image.open(self.image_path).convert('RGB')
			features = tas(np.asanyarray(img))
			return features
		except Exception as e:
			print('\n################# (TAS) - Error in processing!  #################\n', e ,'\n')
