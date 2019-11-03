# FeatureExtraction
Feature extraction - Image Processing

# Install libraries
- OpenCV
- Keras
- mahotas
- numpy


# Use desired code for extraction
########### LBP <br />
from lbp import LBP<br />
lbp = LBP()<br />
featuresLBP = lbp.extractionFeatures('img.jpg')<br />
print('LBP --> ', featuresLBP)<br />
########### ########### ########### <br />
<br />
########### Surf<br />
from surf import Surf<br />
surf = Surf()<br />
featuresSurf= surf.extractionFeatures('img.jpg')<br />
print('Surf --> ', featuresSurf)<br />
########### ########### ########### <br />
<br />
########### Zernike<br />
from zernike import Zernike<br />
zernike = Zernike()<br />
featuresZernike= zernike.extractionFeatures('img.jpg')<br />
print('Zernike --> ', featuresZernike)<br />
########### ########### ########### <br />
<br />
########### Haralick <br />
from haralick import Haralick<br />
haralick = Haralick()<br />
featuresHaralick = haralick.extractionFeatures('img.jpg')<br />
print('haralick --> ', featuresHaralick)<br />
########### ########### ###########  <br />
<br />
########### Deep Features  <br />
from deep import Deep<br />
deep1 = Deep('img.jpg', 'Xception')<br />
featuresDeep1 = deep1.extractionFeatures()<br />
print(featuresDeep1)<br />
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

## Command Line

-d dataset<br />
-- Directory containing the images <br />
-m Method<br />
-- Extraction Method<br />
-n deepName<br />
-- Name desired method to deep learning<br />
<br />

python3 extractor.py -d dataset -m lbp <br />
python3 extractor.py -d dataset -m surf <br />
python3 extractor.py -d dataset -m zernike <br />
python3 extractor.py -d dataset -m haralick <br />
python3 extractor.py -d dataset -m deep -n Xception<br />
python3 extractor.py -d dataset -m deep -n VGG16<br />
python3 extractor.py -d dataset -m deep -n VGG19<br />
python3 extractor.py -d dataset -m deep -n ResNet50<br />
python3 extractor.py -d dataset -m deep -n ResNet101<br />
python3 extractor.py -d dataset -m deep -n ResNet152<br />
python3 extractor.py -d dataset -m deep -n ResNet50V2<br />
python3 extractor.py -d dataset -m deep -n ResNet101V2<br />
python3 extractor.py -d dataset -m deep -n ResNet152V2<br />
python3 extractor.py -d dataset -m deep -n InceptionV3<br />
python3 extractor.py -d dataset -m deep -n InceptionResNetV2<br />
python3 extractor.py -d dataset -m deep -n MobileNet<br />
python3 extractor.py -d dataset -m deep -n MobileNetV2<br />
python3 extractor.py -d dataset -m deep -n DenseNet121<br />
python3 extractor.py -d dataset -m deep -n DenseNet169<br />
python3 extractor.py -d dataset -m deep -n DenseNet201<br />
python3 extractor.py -d dataset -m deep -n NASNetMobile<br />
python3 extractor.py -d dataset -m deep -n NASNetLarge<br />
