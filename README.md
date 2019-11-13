# Introdution

The FeatureExtraction project is dedicated to extracting features from images. We have brought together the main last generation pullers.<br />

You can extract resources by using the following approaches:<br />

1. LBP (Local Binary Part) 
- Extraction            : 352 features 
- Default Configuration : radius = 2 | n_points = 12
- Reference             : OJALA, Timo; PIETIKÄINEN, Matti; MÄENPÄÄ, Topi. Gray scale and rotation invariant texture classification with local binary patterns. In: European Conference on Computer Vision. Springer, Berlin, Heidelberg, 2000. p. 404-420. 
  
2. FOM (First Order Measures)
- Extraction            : 8 features (gray) | 24 features (color)
- First Order Measures  : 1 - Average |  2 - Mode | 3 - Variation | 4 - Standard deviation | 5 - Dispersal | 6 Population sample standard deviation | 7 - Energy | 8 - Entropy
- Reference             : IRONS, James R.; PETERSEN, Gary W. Texture transforms of remote sensing data. Remote Sensing of Environment, v. 11, p. 359-370, 1981.

3. Surf (Speeded up robust features)
- Extraction            : 70 features
- Default Configuration : nr_octaves=4 | nr_scales=6 | initial_step_size=1 | threshold=0.1 | max_points=1024 |  descriptor_only=False
- Reference             : BAY, Herbert; TUYTELAARS, Tinne; VAN GOOL, Luc. Surf: Speeded up robust features. In: European conference on computer vision. Springer, Berlin, Heidelberg, 2006. p. 404-417.

4. Zernike
- Extraction            : 72 features
- Default Configuration : radius = 15 | degree = 8
- Reference             : TEAGUE, Michael Reed. Image analysis via the general theory of moments. JOSA, v. 70, n. 8, p. 920-930, 1980.

5. Haralick 
- Extraction            : 13 features
- Measures              : AngularSecondMoment | Contrast | Correlation | SumofSquares:Variance | InverseDifferenceMoment | SumAverage | SumVariance | SumEntropy | Entropy | DifferenceVariance | DifferenceEntropy | InformationMeasureofCorrelation1 | InformationMeasureofCorrelation2
- Reference             : HARALICK, Robert M.; SHANMUGAM, Karthikeyan; DINSTEIN, Its' Hak. Textural features for image classification. IEEE Transactions on systems, man, and cybernetics, n. 6, p. 610-621, 1973.

6. GCH (Global Color Histogram)
- Extraction            : 30 features
- Default Configuration : bins = 10 (bins for chanel)
- Reference             : STRICKER, Markus Andreas; ORENGO, Markus. Similarity of color images. In: Storage and retrieval for image and video databases III. International Society for Optics and Photonics, 1995. p. 381-392.

7. DEEP Transfer Learning
- Extraction            : Depends on the approach. (512 to 4032 features)
- Approach              : Xception | VGG16 | VGG19 | ResNet50 | ResNet101 | ResNet152 | ResNet50V2 | ResNet101V2 | ResNet152V2 | InceptionV3 | InceptionResNetV2 | MobileNet | MobileNetV2 | DenseNet121 | DenseNet169 | DenseNet201 | NASNetMobile | NASNetLarge 
- Reference             :

# Requirements
- Tests performed on Ubuntu 18.04.3 LTS with Python (3.6.8) 
## libraries
- OpenCV (4.0.1)
- Keras (2.3.1) 
- TensorFlow (2.0.0)
- mahotas (1.4.8)
- numpy (1.17.1)

# Use desired code for extraction
########### LBP - Local Binary Part <br />
`from extractor.lbp import LBP`
<br />
`lbp = LBP()`
<br />
`featuresLBP = lbp.extractionFeatures('img.jpg')`
<br />
`print('LBP --> ', featuresLBP)`
<br />
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
########### FOM - First Order Measures (Gray)<br />
from extractor.fom import FOM<br />
fom = FOM()<br />
featuresFOM = fom.extractionFeatures('img.jpg')<br />
print('FOM (Gray) --> ', featuresFOM)<br />
########### ########### ###########  <br />
<br />
########### FOM - First Order Measures (Color)<br />
from extractor.fom import FOM<br />
fom = FOM()<br />
featuresFOM = fom.extractionFeaturesColor('img.jpg')<br />
print('FOM (Color) --> ', featuresFOM)<br />
########### ########### ###########  <br />
<br />
########### GCH - Global Color Histogram<br />
from extractor.gch import GCH<br />
gch = GCH()<br />
featuresGCH = gch.extractionFeatures('img.jpg')<br />
print('GCH --> ', featuresGCH)<br />
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
python3 extractor.py -d dataset -m fom <br />
python3 extractor.py -d dataset -m fomc <br />
python3 extractor.py -d dataset -m gch <br />
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
