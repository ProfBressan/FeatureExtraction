
# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - BIC
dependencies : PIL (Python Imaging Library) 
References   :
    ----------
    STEHLING, Renato O.; NASCIMENTO, Mario A.; FALCAO, Alexandre X. 
    A compact and efficient image retrieval approach based on border/interior pixel classification. 
    In: Proceedings of the eleventh international conference on Information and knowledge management.
    2002. p. 102-109.

Using        : 
	from bic import BIC
	bic = BIC() // default BIC(64) --> 128 bins
	featuresBIC = bic.extractionFeatures('img.jpg')
	print('BIC --> ', featuresBIC)
"""

from PIL import Image

class BIC:
    def __init__(self, factor = 64):
        self.image_path = ''
        self.factor = factor
    def setImagePath(self, image_path):
        self.image_path = image_path
    def getImagePath(self):
        return self.image_path
    def extractionFeatures(self, image_path):
        try:
            self.image_path = image_path
            img = Image.open(self.image_path).convert('RGB').convert('L')
            HI,HE = [0] * self.factor, [0] * self.factor
            N, M = img.size
            for x in range(N):
                for y in range(M):
                    ind = int((img.getpixel((x,y)) / 255) * (self.factor-1))
                    if (x == 0 or y ==0 or x+1 == N or y+1 == M):
                        HE[ind] += 1
                    else:
                        if (img.getpixel((x,y)) == img.getpixel((x,y-1)) and 
                                img.getpixel((x,y)) == img.getpixel((x,y+1)) and 
                                img.getpixel((x,y)) == img.getpixel((x-1,y)) and 
                                img.getpixel((x,y)) == img.getpixel((x+1,y)) ):
                            HI[ind] += 1
                        else:
                            HE[ind] += 1
            return HI + HE
        except Exception as e:
            print('\n################# (BIC) - Error in processing!  #################\n', e)
