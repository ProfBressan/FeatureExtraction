# -*- coding: utf-8 -*-
"""
Author       : Rafael S. Bressan
Date         : 31/10/2019
Contact      : https://www.linkedin.com/in/profbressan/ 

Description  : Features Extraction - FOM (First Order Measures)
Dependencies : PIL (Python Imaging Library) | math | os | sys | statistics
First Order Measures : 1 - Average |  2 - Mode | 3 - Variation | 
                       4 - Standard deviation | 5 - Dispersal | 
                       6 Population sample standard deviation | 7 - Energy | 8 - Entropy
                       #9 - High median of data | #10 - Low median of data
Using        : 
	from fom import FOM
	fom = FOM()
	featuresFOM = fom.extractionFeatures('img.jpg')
	print('First Order Measures (Gray) --> ', featuresFOM)
    featuresFOMColor = fom.extractionFeaturesColor('img.jpg')
	print('First Order Measures (Color) --> ', featuresFOMColor)
"""
from PIL import Image
import math, os, sys, statistics 

class FOM:
    def __init__(self):
        self.image_path = ''
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
            v, features = [],[]
            maxHistogram = 256
            hist = [0] * maxHistogram
            Hg = 0
            for i in range(imgGray.size[0]):
                for j in range(imgGray.size[1]):
                    r = imgGray.getpixel((i,j))
                    v.append(r)
                    hist[r] += 1
                    if (r > Hg):
                        Hg = r
            features.append(statistics.mean(v)) # Arithmetic mean (“average”) of data.
            features.append(statistics.mode(v)) # Single mode (most common value) of discrete or nominal data.
            features.append(statistics.pvariance(v)) # Population variance of data.
            features.append(statistics.pstdev(v)) # Population standard deviation of data.
            features.append(statistics.variance(v)) # Sample variance of data.
            features.append(statistics.stdev(v)) # Sample standard deviation of data
            entropy, energy = 0, 0
            for i in range(Hg): 
                energy += (hist[i] ** 2)
                if (hist[i] != 0):
                    entropy += -hist[i] * math.log2(hist[i])
            features.append(energy) # Energy
            features.append(entropy) # Entropy
            #features.append(statistics.median_high(v)) # High median of data.
            #features.append(statistics.median_low(v)) # Low median of data.
            return features
        except Exception as e:
            print('\n################# (FOM) - Error in processing! #################\n', e)
    
    def extractionFeaturesColor(self, image_path):
        self.image_path = image_path
        try:
            imgIN = Image.open(self.image_path) 
            img = imgIN.convert('RGB')
            vr, vg, vb, features = [],[],[],[]
            maxHistogram = 256
            histR,histG,histB  = [0] * maxHistogram, [0] * maxHistogram, [0] * maxHistogram
            HgR, HgG, HgB = 0,0,0
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    r, g, b = img.getpixel((i,j))
                    vr.append(r), vg.append(g), vb.append(b)
                    histR[r] += 1
                    histG[g] += 1
                    histB[b] += 1 
                    if (r > HgR):
                        HgR = r
                    if (g > HgG):
                        HgG = g
                    if (b > HgB):
                        HgB = b
            features.append(statistics.mean(vr)) , features.append(statistics.mean(vg)), features.append(statistics.mean(vb)) 
            features.append(statistics.mode(vr)), features.append(statistics.mode(vg)), features.append(statistics.mode(vb))
            features.append(statistics.pvariance(vr)), features.append(statistics.pvariance(vg)), features.append(statistics.pvariance(vb)) 
            features.append(statistics.pstdev(vr)), features.append(statistics.pstdev(vg)), features.append(statistics.pstdev(vb)) 
            features.append(statistics.variance(vr)), features.append(statistics.variance(vg)), features.append(statistics.variance(vb)) 
            features.append(statistics.stdev(vr)), features.append(statistics.stdev(vg)), features.append(statistics.stdev(vb))
            entropyR, entropyG, entropyB = 0,0,0
            energyR, energyG, energyB = 0,0,0
            for i in range(HgR): 
                energyR += (histR[i] ** 2)
                if (histR[i] != 0):
                    entropyR += -histR[i] * math.log2(histR[i])
            for i in range(HgG):
                if (histG[i] != 0):
                    entropyG += -histG[i] * math.log2(histG[i])
                energyG += (histG[i] ** 2)
            for i in range(HgB):  
                energyB += (histB[i] ** 2)
                if (histB[i] != 0):
                    entropyB += -histB[i] * math.log2(histB[i])
            features.append(energyR), features.append(energyG), features.append(energyB) # Energy 
            features.append(entropyR), features.append(entropyG), features.append(entropyB) # Entropy
            #features.append(statistics.median_high(vr)) , features.append(statistics.median_high(vg)), features.append(statistics.median_high(vb))  
            #features.append(statistics.median_low(vr)) , features.append(statistics.median_low(vg)), features.append(statistics.median_low(vb)) 
            return features
        except Exception as e:
            print('\n################# (FOMC) - Error in processing!  #################\n', e)