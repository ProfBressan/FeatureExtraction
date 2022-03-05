# Introdution

The FeatureExtraction project is dedicated to extracting features from images.

You can extract features using the following approaches:<br />

1. BIC (Border/Interior Pixel Classification)
- Extraction            : 128 features
- Default Configuration : bins = 64 ((HI 64 + HC 64 = 128))
- Reference             : STEHLING, Renato O.; NASCIMENTO, Mario A.; FALCAO, Alexandre X. A compact and efficient image retrieval approach based on border/interior pixel classification. In: Proceedings of the eleventh international conference on Information and knowledge management. 2002. p. 102-109. 

2. TAS (Threshold Adjacency Statistics)
- Extraction            : 162 features
- Reference             : COELHO, Luís Pedro et al. Structured literature image finder: extracting information from text and images in biomedical literature. In: Linking Literature, Information, and Knowledge for Biology. Springer, Berlin, Heidelberg, 2010. p. 23-32.

3. LBP (Local Binary Part) 
- Extraction            : 352 features 
- Default Configuration : radius = 2 | n_points = 12
- Reference             : OJALA, Timo; PIETIKÄINEN, Matti; MÄENPÄÄ, Topi. Gray scale and rotation invariant texture classification with local binary patterns. In: European Conference on Computer Vision. Springer, Berlin, Heidelberg, 2000. p. 404-420. 
  
4. FOM (First Order Measures)
- Extraction            : 8 features (gray) | 24 features (color)
- First Order Measures  : 1 - Average |  2 - Mode | 3 - Variation | 4 - Standard deviation | 5 - Dispersal | 6 Population sample standard deviation | 7 - Energy | 8 - Entropy
- Reference             : IRONS, James R.; PETERSEN, Gary W. Texture transforms of remote sensing data. Remote Sensing of Environment, v. 11, p. 359-370, 1981.

5. Zernike
- Extraction            : 72 features
- Default Configuration : radius = 15 | degree = 8
- Reference             : TEAGUE, Michael Reed. Image analysis via the general theory of moments. JOSA, v. 70, n. 8, p. 920-930, 1980.

6. Haralick 
- Extraction            : 13 features
- Measures              : AngularSecondMoment | Contrast | Correlation | SumofSquares:Variance | InverseDifferenceMoment | SumAverage | SumVariance | SumEntropy | Entropy | DifferenceVariance | DifferenceEntropy | InformationMeasureofCorrelation1 | InformationMeasureofCorrelation2
- Reference             : HARALICK, Robert M.; SHANMUGAM, Karthikeyan; DINSTEIN, Its' Hak. Textural features for image classification. IEEE Transactions on systems, man, and cybernetics, n. 6, p. 610-621, 1973.

7. GCH (Global Color Histogram)
- Extraction            : 30 features
- Default Configuration : bins = 10 (bins for chanel)
- Reference             : STRICKER, Markus Andreas; ORENGO, Markus. Similarity of color images. In: Storage and retrieval for image and video databases III. International Society for Optics and Photonics, 1995. p. 381-392.

8. DEEP Transfer Learning
- Extraction            : Depends on the approach. (512 to 4032 features)
- Approach              : Xception | VGG16 | VGG19 | ResNet50 | ResNet50V2 | ResNet101 | ResNet101V2 | ResNet152 | ResNet152V2 | InceptionV3 | InceptionResNetV2 | MobileNet | MobileNetV2 | DenseNet121 | DenseNet169 | DenseNet201 | NASNetMobile | NASNetLarge | EfficientNetB0 | EfficientNetB1 | EfficientNetB2 | EfficientNetB3 | EfficientNetB4 | EfficientNetB5 | EfficientNetB6 | EfficientNetB7 | EfficientNetV2B0 | EfficientNetV2B1 | EfficientNetV2B2 | EfficientNetV2B3 | EfficientNetV2S | EfficientNetV2M | EfficientNetV2L  

# Requirements
- Tests performed on Ubuntu 20.04.4 LTS with Python (3.8.10) 

## libraries
- see the file (requirements.txt)
- Install all dependencies (pip3 install -r requirements.txt)

# Use the desired code for extraction directly in your program<br />

- TAS (Threshold Adjacency Statistics)<br />
`from extraction.tas import TAS`<br />
`tas = TAS()`<br />
`featuresTAS = tas.extractionFeatures('img.jpg')`<br />
`print('TAS --> ', featuresTAS)`<br />
<br />

- BIC (Border/Interior pixel Classification)<br />
`from extraction.bic import BIC`<br />
`bic = BIC()`<br />
`featuresBIC = bic.extractionFeatures('img.jpg')`<br />
`print('BIC --> ', featuresBIC)`<br />
<br />

- LBP (Local Binary Part)<br />
`from extraction.lbp import LBP`<br />
`lbp = LBP()`<br />
`featuresLBP = lbp.extractionFeatures('img.jpg')`<br />
`print('LBP --> ', featuresLBP)`<br />
<br />

- Zernike<br />
`from extraction.zernike import Zernike`<br />
`zernike = Zernike()`<br />
`featuresZernike= zernike.extractionFeatures('img.jpg')`<br />
`print('Zernike --> ', featuresZernike)`<br />
<br />

- Haralick <br />
`from extraction.haralick import Haralick`<br />
`haralick = Haralick()`<br />
`featuresHaralick = haralick.extractionFeatures('img.jpg')`<br />
`print('haralick --> ', featuresHaralick)`<br />
<br />

- FOM - First Order Measures (Gray) <br />
`from extraction.fom import FOM`<br />
`fom = FOM()`<br />
`featuresFOM = fom.extractionFeatures('img.jpg')`<br />
`print('FOM (Gray) --> ', featuresFOM)`<br />
<br />

- FOM - First Order Measures (Color)<br />
`from extraction.fom import FOM`<br />
`fom = FOM()`<br />
`featuresFOM = fom.extractionFeaturesColor('img.jpg')`<br />
`print('FOM (Color) --> ', featuresFOM)`<br />
<br />

- GCH - Global Color Histogram<br />
`from extraction.gch import GCH`<br />
`gch = GCH()`<br />
`featuresGCH = gch.extractionFeatures('img.jpg')`<br />
`print('GCH --> ', featuresGCH)`<br />
<br />

- Deep Features  <br />
`from extraction.deep import Deep`<br />
`deep = Deep('Xception')`<br />
`featuresDeep = deep.extractionFeatures('img.jpg')`<br />
`print(featuresDeep)`<br />

Opition - DEEP:<br />
--- Xception <br />
--- VGG16 <br />
--- VGG19 <br />
--- ResNet50 <br />
--- ResNet50V2 <br />
--- ResNet101 <br />
--- ResNet101V2 <br />
--- ResNet152 <br />
--- ResNet152V2 <br />
--- InceptionV3 <br />
--- InceptionResNetV2 <br />
--- MobileNet <br />
--- MobileNetV2 <br />
--- DenseNet121 <br />
--- DenseNet169 <br />
--- DenseNet201 <br />
--- NASNetMobile <br />
--- NASNetLarge <br />
--- EfficientNetB0 <br />
--- EfficientNetB1 <br />
--- EfficientNetB2 <br />
--- EfficientNetB3 <br /> 
--- EfficientNetB4 <br />
--- EfficientNetB5 <br />
--- EfficientNetB6 <br />
--- EfficientNetB7 <br />
--- EfficientNetV2B0 <br />
--- EfficientNetV2B1 <br />
--- EfficientNetV2B2 <br />
--- EfficientNetV2B3 <br />
--- EfficientNetV2S <br />
--- EfficientNetV2M <br />
--- EfficientNetV2L <br />

# Extract from multiple simultaneous images and generate one file (.arff)

1. Organize o conjunto de imagens

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

2. Run the command for extraction using a specific technique
## Command Line
-d dataset<br />
-- Directory containing the images <br />
-m Method<br />
-- Extraction Method<br />
-n deepName<br />
-- Name desired method to deep learning<br />
<br />

```
python3 extractorFeatures.py -d dataset -m tas
python3 extractorFeatures.py -d dataset -m bic
python3 extractorFeatures.py -d dataset -m lbp
python3 extractorFeatures.py -d dataset -m zernike
python3 extractorFeatures.py -d dataset -m haralick
python3 extractorFeatures.py -d dataset -m fom
python3 extractorFeatures.py -d dataset -m fomc
python3 extractorFeatures.py -d dataset -m gch
python3 extractorFeatures.py -d dataset -m deep -n Xception
python3 extractorFeatures.py -d dataset -m deep -n VGG16
python3 extractorFeatures.py -d dataset -m deep -n VGG19
python3 extractorFeatures.py -d dataset -m deep -n ResNet50
python3 extractorFeatures.py -d dataset -m deep -n ResNet50V2
python3 extractorFeatures.py -d dataset -m deep -n ResNet101
python3 extractorFeatures.py -d dataset -m deep -n ResNet101V2
python3 extractorFeatures.py -d dataset -m deep -n ResNet152
python3 extractorFeatures.py -d dataset -m deep -n ResNet152V2
python3 extractorFeatures.py -d dataset -m deep -n InceptionV3
python3 extractorFeatures.py -d dataset -m deep -n InceptionResNetV2
python3 extractorFeatures.py -d dataset -m deep -n MobileNet
python3 extractorFeatures.py -d dataset -m deep -n MobileNetV2
python3 extractorFeatures.py -d dataset -m deep -n DenseNet121
python3 extractorFeatures.py -d dataset -m deep -n DenseNet169
python3 extractorFeatures.py -d dataset -m deep -n DenseNet201
python3 extractorFeatures.py -d dataset -m deep -n NASNetMobile
python3 extractorFeatures.py -d dataset -m deep -n NASNetLarge
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB0
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB1
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB2
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB3
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB4
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB5
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB6
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetB7
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2B0
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2B1
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2B2
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2B3
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2S
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2M
python3 extractorFeatures.py -d dataset -m deep -n EfficientNetV2L
```

3. Run command for extraction considering all approaches
```
$ ./autoExtract.sh

```

4. Generated files (.arff)

The generated files will be available in the (output_files) directory after the execution

- Observation.
If desired, you can transform (.arff) to standard (csv) using the file (arff_to_csv.py)
```
python3 arff_to_csv.py -d bic.arff

```

5. Example of reading the generated files

- Reading from (csv) file
```
import pandas as pd

df = pd.read_csv('bic.csv')
print(df.head())
...
```

- Reading from (arff) file
```
from scipy.io.arff import loadarff
import pandas as pd
dataset, mdataset = loadarff("bic.arff")
df = pd.DataFrame(dataset)
print(df.head())
```

# Reference
Bressan, R. S., Alves, D. H., Valerio, L. M., Bugatti, P. H., & Saito, P. T. (2018, June). DOCToR: the role of deep features in content-based mammographic image retrieval. In 2018 IEEE 31st International Symposium on Computer-Based Medical Systems (CBMS) (pp. 158-163). IEEE.