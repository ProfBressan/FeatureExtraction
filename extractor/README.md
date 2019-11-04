# FeatureExtraction
Feature extraction - Image Processing

- Tests performed on Ubuntu 18.04.3 LTS with Python (3.6.8) 

# Install libraries
- OpenCV (4.0.1)
- Keras (2.3.1) 
- mahotas (1.4.8)
- numpy (1.17.1)


# Use desired code for extraction
########### LBP <br />
from extractor.lbp import LBP<br />
lbp = LBP()<br />
featuresLBP = lbp.extractionFeatures('img.jpg')<br />
print('LBP --> ', featuresLBP)<br />
########### ########### ########### <br />
<br />
########### Surf<br />
from extractor.surf import Surf<br />
surf = Surf()<br />
featuresSurf= surf.extractionFeatures('img.jpg')<br />
print('Surf --> ', featuresSurf)<br />
########### ########### ########### <br />
<br />
########### Zernike<br />
from extractor.zernike import Zernike<br />
zernike = Zernike()<br />
featuresZernike= zernike.extractionFeatures('img.jpg')<br />
print('Zernike --> ', featuresZernike)<br />
########### ########### ########### <br />
<br />
########### Haralick <br />
from extractor.haralick import Haralick<br />
haralick = Haralick()<br />
featuresHaralick = haralick.extractionFeatures('img.jpg')<br />
print('haralick --> ', featuresHaralick)<br />
########### ########### ###########  <br />
<br />
########### Deep Features  <br />
from extractor.deep import Deep<br />
deep = Deep('Xception')<br />
featuresDeep = deep.extractionFeatures('img.jpg')<br />
print(featuresDeep)<br />
####### Opition - DEEP:<br />
--- Xception<br />
--- VGG16<br />
--- VGG19 <br />
--- ResNet50 <br />
--- ResNet101<br />
--- ResNet152<br />
--- ResNet50V2<br />
--- ResNet101V2<br />
--- ResNet152V2<br />
--- InceptionV3<br />
--- InceptionResNetV2<br />
--- MobileNet<br />
--- MobileNetV2<br />
--- DenseNet121<br />
--- DenseNet169<br />
--- DenseNet201<br />
--- NASNetMobile<br />
--- NASNetLarge<br />


# Extract from multiple simultaneous images and generate one file (.arff)
- Orgnization dataset<br />
-- Dir_dataset<br />
------ Dir_class1<br />
------------- img01.jpg<br />
------------- img02.jpg<br />
------------- img03.jpg<br />
------ Dir_class2<br />
------------- img01.jpg<br />
------------- img02.jpg<br />
------------- img03.jpg<br />
------ Dir_classN<br />
------------- img01.jpg<br />
------------- img02.jpg<br />
------------- img03.jpg<br />
