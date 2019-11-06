# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com / (43)99924-9391

Description  : Features Extraction - Deep Learning 
dependencies : keras | numpy
References   :
    ----------
    CHOLLET, François. Xception: Deep learning with depthwise separable 
    convolutions. In: Proceedings of the IEEE conference on computer vision 
    and pattern recognition. 2017. p. 1251-1258.


    
"""
import os
from keras import applications
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
import numpy as np

class Deep:
	def __init__(self, modelName):
		self.width, self.height = 224, 224
		self.image_path = ''
		self.modelName = modelName
		if self.modelName == 'Xception':
			self.model = applications.xception.Xception(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 299, 299
		if self.modelName == 'VGG16':
			self.model = applications.vgg16.VGG16(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'VGG19':
			self.model = applications.vgg19.VGG19(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'ResNet50':
			self.model = applications.resnet.ResNet50(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'ResNet101':
			self.model = applications.resnet.ResNet101(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'ResNet152':
			self.model = applications.resnet.ResNet152(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'ResNet50V2':
			self.model = applications.resnet_v2.ResNet50V2(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'ResNet101V2':
			self.model = applications.resnet_v2.ResNet101V2(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'ResNet152V2':
			self.model = applications.resnet_v2.ResNet152V2(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'InceptionV3':
			self.model = applications.inception_v3.InceptionV3(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 299, 299
		if self.modelName == 'InceptionResNetV2':
			self.model = applications.inception_resnet_v2.InceptionResNetV2(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 299, 299
		if self.modelName == 'MobileNet':
			self.model = applications.mobilenet.MobileNet(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'MobileNetV2':
			self.model = applications.mobilenet_v2.MobileNetV2(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'DenseNet121':
			self.model = applications.densenet.DenseNet121(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'DenseNet169':
			self.model = applications.densenet.DenseNet169(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'DenseNet201':
			self.model = applications.densenet.DenseNet201(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'NASNetMobile':
			self.model = applications.nasnet.NASNetMobile(weights='imagenet', include_top=False, pooling='avg')
		if self.modelName == 'NASNetLarge':
			self.model = applications.nasnet.NASNetLarge(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 331, 331

	def setImagePath(self, image_path):
		self.image_path = image_path
	def getImagePath(self):
		return self.image_path
	def extractionFeatures(self, image_path):
		self.image_path = image_path
		try:
			img = image.load_img(self.image_path, target_size=(self.width, self.height))	
			x = image.img_to_array(img)
			x = np.expand_dims(x, axis=0)
			x = preprocess_input(x)
			features = self.model.predict(x)[0]
			arrayFeatures = np.char.mod('%f', features)
			return arrayFeatures
		except Exception as e:
			print('\n################# (Deep) - Error Reading Image!  #################\n')
