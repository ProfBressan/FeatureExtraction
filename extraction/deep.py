# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - Deep Learning 
dependencies : tensorflow | numpy
References   :
    ----------
    CHOLLET, François. Xception: Deep learning with depthwise separable 
    convolutions. In: Proceedings of the IEEE conference on computer vision 
    and pattern recognition. 2017. p. 1251-1258.

Using        : 
	from deep import Deep
	deep = Deep("Xception") //  Xception | VGG16 | VGG19 | ResNet50 | ResNet101 | ResNet152 | ResNet50V2 | ResNet101V2 | ResNet152V2 | InceptionV3 | InceptionResNetV2 | MobileNet | MobileNetV2 | DenseNet121 | DenseNet169 | DenseNet201 | NASNetMobile | NASNetLarge
	featuresDeep = deep.extractionFeatures('img.jpg')
	print('Deep --> ', featuresDeep)
"""
import tensorflow as tf
import numpy as np

class Deep:
	def __init__(self, modelName):
		self.width, self.height = 224, 224
		self.image_path = ''
		self.modelName = modelName
		if self.modelName == 'Xception':
			self.model = tf.keras.applications.xception.Xception(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 299, 299
		elif self.modelName == 'VGG16':
			self.model = tf.keras.applications.vgg16.VGG16(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'VGG19':
			self.model = tf.keras.applications.vgg19.VGG19(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'ResNet50':
			self.model = tf.keras.applications.resnet.ResNet50(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'ResNet101':
			self.model = tf.keras.applications.resnet.ResNet101(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'ResNet152':
			self.model = tf.keras.applications.resnet.ResNet152(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'ResNet50V2':
			self.model = tf.keras.applications.resnet_v2.ResNet50V2(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'ResNet101V2':
			self.model = tf.keras.applications.resnet_v2.ResNet101V2(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'ResNet152V2':
			self.model = tf.keras.applications.resnet_v2.ResNet152V2(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'RegNetX002':
			self.model = tf.keras.applications.regnet.RegNetX002(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB0':
			self.model = tf.keras.applications.efficientnet.EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB1':
			self.model = tf.keras.applications.efficientnet.EfficientNetB1(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB2':
			self.model = tf.keras.applications.efficientnet.EfficientNetB2(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB3':
			self.model = tf.keras.applications.efficientnet.EfficientNetB3(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB4':
			self.model = tf.keras.applications.efficientnet.EfficientNetB4(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB5':
			self.model = tf.keras.applications.efficientnet.EfficientNetB5(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB6':
			self.model = tf.keras.applications.efficientnet.EfficientNetB6(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetB7':
			self.model = tf.keras.applications.efficientnet.EfficientNetB7(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2B0':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2B0(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2B1':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2B1(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2B2':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2B2(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2B3':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2B3(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2L':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2L(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2M':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2M(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'EfficientNetV2S':
			self.model = tf.keras.applications.efficientnet_v2.EfficientNetV2S(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'InceptionV3':
			self.model = tf.keras.applications.inception_v3.InceptionV3(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 299, 299
		elif self.modelName == 'InceptionResNetV2':
			self.model = tf.keras.applications.inception_resnet_v2.InceptionResNetV2(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 299, 299
		elif self.modelName == 'MobileNet':
			self.model = tf.keras.applications.mobilenet.MobileNet(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'MobileNetV2':
			self.model = tf.keras.applications.mobilenet_v2.MobileNetV2(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'DenseNet121':
			self.model = tf.keras.applications.densenet.DenseNet121(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'DenseNet169':
			self.model = tf.keras.applications.densenet.DenseNet169(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'DenseNet201':
			self.model = tf.keras.applications.densenet.DenseNet201(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'NASNetMobile':
			self.model = tf.keras.applications.nasnet.NASNetMobile(weights='imagenet', include_top=False, pooling='avg')
		elif self.modelName == 'NASNetLarge':
			self.model = tf.keras.applications.nasnet.NASNetLarge(weights='imagenet', include_top=False, pooling='avg')
			self.width, self.height = 331, 331

	def setImagePath(self, image_path):
		self.image_path = image_path
	def getImagePath(self):
		return self.image_path
	def extractionFeatures(self, image_path):
		self.image_path = image_path
		try:
			img = tf.keras.preprocessing.image.load_img(self.image_path, target_size=(self.width, self.height))	
			x = tf.keras.preprocessing.image.img_to_array(img)
			x = np.expand_dims(x, axis=0)
			x = tf.keras.applications.resnet50.preprocess_input(x)
			features = self.model.predict(x)[0]
			arrayFeatures = np.char.mod('%f', features)
			return arrayFeatures
		except Exception as e:
			print('\n################# (Deep) - Error in processing!  #################\n')
