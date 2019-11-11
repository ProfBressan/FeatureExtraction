# -*- coding: utf-8 -*-
"""
Author       : Rafael Staiger Bressan
Date         : 31/10/2019
Contact      : profbressan@gmail.com 

Description  : Features Extraction - GCH (Global Color Histogram)
Dependencies : PIL (Python Imaging Library) 
Features     : 30 Features (10 bins per (channel))
Reference    :
               STRICKER, Markus Andreas; ORENGO, Markus. Similarity of color images. 
               In: Storage and retrieval for image and video databases III. International 
               Society for Optics and Photonics, 1995. p. 381-392.

Using        : 
	from gch import GCH
	fom = GCH()
	featuresGCH = gch.extractionFeatures('img.jpg')
	print('GCH --> ', featuresGCH)
"""
from PIL import Image

class GCH:
    def __init__(self):
	    self.image_path = ''
    def setImagePath(self, image_path):
        self.image_path = image_path
    def getImagePath(self):
        return self.image_path
    def extractionFeatures(self, image_path):
        self.image_path = image_path
        try:
            imgIN = Image.open(self.image_path) 
            img = imgIN.convert('RGB')
            bins = 10 # bins per (channel)
            evolution = (255/bins)
            features = []
            histR,histG,histB  = [0] * bins, [0] * bins, [0] * bins
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    r, g, b = img.getpixel((i,j))
                    lookBin = 0
                    controlR = evolution
                    contR, contG, contB = 0,0,0
                    while(lookBin == 0):
                        contR += 1
                        if (r <= controlR):
                            r = controlR
                            lookBin = 1
                        else:
                            controlR += evolution
                            if (controlR >= 255):
                                controlR = 255 
                    lookBin = 0
                    controlG = evolution
                    while(lookBin == 0):
                        contG += 1
                        if (g <= controlG):
                            g = controlG
                            lookBin = 1
                        else:
                            controlG += evolution
                            if (controlG >= 255):
                                controlG = 255
                    lookBin = 0
                    controlB = evolution                    
                    while(lookBin == 0):
                        contB += 1
                        if (b <= controlB):
                            b = controlB
                            lookBin = 1
                        else:
                            controlB += evolution
                            if (controlB >= 255):
                                controlB = 255
                    histR[contR-1] += 1
                    histG[contG-1] += 1
                    histB[contB-1] += 1
            
            features = histR + histG + histB
            #print('Size --> ', len(features))
            return features
        except Exception as e:
            print('\n################# (LBP) - Error Reading Image!  #################\n', e)