#Ai Art Generator

###Autorzy
Kacper Kaczor
Karol Niemykin

###Cel zadania
Celem zadania byo stworzenie obrazu za pomocą sztucznej inteligencji i sieci neuronowych. Do stworzenia rozwiązania urzyliśmy bibliotek:
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)

# Troche Teorii

###Konwulacyjne sieci neuronowe (CNN)

Najczęściej konwulacyjne sieci neuronowe są używane do przetwarzania obrazów.
CNN to algorytm, który może pobrać obraz wejściowy i sklasyfikować go wedle predefiniowanych kategorii (np. rasy psa). Jest to możliwe dzięki przypisaniu wag różnym kształtom, strukturom, obiektom.

 
Sieci konwolucyjne poprzez trening są w stanie nauczyć się, jakie cechy szczególne obrazu pomagają w jego klasyfikacji. Ich przewagą nad standardowymi sieciami głębokimi jest większa skuteczność w wykrywaniu zawiłych zależności w obrazach. Jest to możliwe dzięki zastosowaniu filtrów badających zależności pomiędzy sąsiednimi pikselami.

W naszym przykładzie dzieki temu obraz bazowy dalej zachowuje swój kształt i sens. Postacie na obrazie dalej bedą rozpoznawalne. 

Każdy obraz jest macierzą wartości, których liczba jest proporcjonalna do jego szerokości i wysokości w pikselach. W przypadku obrazów RGB obraz cechują trzy kolory podstawowe, więc każdy piksel reprezentowany jest przez trzy wartości. Zadaniem CNN jest redukcja rozmiaru obrazu do lżejszej formy bez utraty wartościowych cech, czyli tych które niosą informacje kluczowe dla klasyfikacji.

![](https://bfirst.tech/wp-content/uploads/2019/06/sieci_konwolucyjne_gif-1.gif)

Powyższa animacja przedstawia obraz RGB oraz poruszający się po nim filtr o rozmiarze 3x3x3 i zdefiniowanym kroku. Krok to wartość w pikselach, o którą przesuwa się filtr. Może zostać zastosowany „zero padding”, czyli wypełnienie zerami (białe kwadraty). Taki zabieg pozwala na zachowanie większej ilości informacji, kosztem wydajności.

Kolejne wartości macierzy wyjściowej obliczane są w następujący sposób:

mnożenie wartości w danym fragmencie obrazu przez filtr (po elementach),
sumowanie obliczonych wartości dla danego kanału,
sumowanie wartości dla każdego kanału z uwzględnieniem biasu (w tym przypadku równego 1).
 
Warto zwrócić uwagę, że wartości filtru dla danego kanału mogą się od siebie różnić. Zadaniem warstwy konwolucyjnej, w przypadku pierwszej warstwy, jest wyodrębnienie cech, takich jak krawędzie, kolory, gradienty. Im więcej warstw, tym bardziej skomplikowane cechy zostaną wyznaczone.

 
Analogicznie do warstw zwykłej sieci, po warstwie konwolucyjnej występuje warstwa aktywacyjna (najczęściej funkcja ReLU), wprowadzająca nieliniowość do sieci.

 
Druga warstwa jest nazywana łączącą (pooling layer). Jej zadaniem jest zmniejszenie wymiarów cech konwolucyjnych, wyznaczonych w poprzedniej warstwie, przy zachowaniu kluczowych cech. Odpowiada również za redukcję szumu. Najpopularniejszą metodą jest „max pooling”.

![](https://bfirst.tech/wp-content/uploads/2019/06/sieci_konwolucyjne_2-600x286.png)

Operacja łączenia przebiega w sposób zbliżony do stosowanego w warstwie konwolucyjnej. Definiowany jest filtr oraz krok. Kolejne wartości macierzy wyjściowej są maksymalną wartością objętą filtrem.

 
Wymienione warstwy stanowią razem jedną warstwę sieci konwolucyjnej. Po zastosowaniu wybranej ilości warstw otrzymana macierz zostaje spłaszczona i stanowi wejście do standardowej sieci neuronowej, stworzonej z w pełni połączonych warstw. Pozwala to na nauczenie algorytmu nieliniowych zależności pomiędzy cechami wyznaczonymi przez warstwy konwolucyjne.

 
Ostatnią warstwą sieci jest warstwa Soft-Max, pozwalająca na uzyskanie wartości prawdopodobieństw przynależności do poszczególnych klas (na przykład prawdopodobieństwo, że na obrazie znajduje się kot). W trakcie treningu są one porównywane z pożądanym wynikiem klasyfikacji w zastosowanej funkcji kosztu, a następnie poprzez algorytm wstecznej propagacji sieć dostosowuje swoje wagi w celu zminimalizowania błędu.

Konwolucyjne sieci neuronowe są ważnym elementem rozwoju uczenia maszynowego. Przyczyniają się do postępu automatyzacji i pozwalają rozszerzyć ludzkie zdolności percepcji. Ich możliwości będą stale rosnąć wraz z mocą obliczeniową komputerów i ilością dostępnych danych.

#Nasz Kod

Zaczeliśmy od importowania biblliotek oraz sprawdziliśmy wersje Pythona TensorFlow oraz Keras. Nasz kod działa poprawnie z TensorFlow 1.13.1, 
więc ta wersja jest rekomendowana.

```Python
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from PIL import Image
from keras import backend as K
from keras.preprocessing.image import load_img, img_to_array
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input
from scipy.optimize import fmin_l_bfgs_b
import time

print(sys.version)
print(tf.__version__)
print(keras.__version__)
```
oraz deklaracji danych

```Python
cImPath = 'base_image.jpg'
sImPath = 'reference_image.jpg'
genImOutputPath = 'output.jpg'
```

Następnie ustawiliśmy rozmiar naszych obrazów na 512px, oraz ustawiliśmy procesowanie obrazów zmienne `cImArr`, `sImArr` oraz `gIm0` dotyczą usprawnienia wykonywania skryptu poprzez procesor GPU. Typy `float32` i `float64` pomagają w uniknięciu błędów procesora graficznego.

```Python
targetHeight = 512
targetWidth = 512
targetSize = (targetHeight, targetWidth)

cImageOrig = Image.open(cImPath)
cImageSizeOrig = cImageOrig.size
cImage = load_img(path=cImPath, target_size=targetSize)
cImArr = img_to_array(cImage)
cImArr = K.variable(preprocess_input(np.expand_dims(cImArr, axis=0)), dtype='float32')

sImage = load_img(path=sImPath, target_size=targetSize)
sImArr = img_to_array(sImage)
sImArr = K.variable(preprocess_input(np.expand_dims(sImArr, axis=0)), dtype='float32')

gIm0 = np.random.randint(256, size=(targetWidth, targetHeight, 3)).astype('float64')
gIm0 = preprocess_input(np.expand_dims(gIm0, axis=0))

gImPlaceholder = K.placeholder(shape=(1, targetWidth, targetHeight, 3))
```
Kolejnym krokiem jest definiowanie funkcji stratnych. Te funkcje pomagają utrzymać nam sens samego obrazu. Krawędzie pozostają na swoim miejscu. Jesteś w stanie rozpoznać np. głowę, uszy, nos etc. Zastosowana jest również Macierz Grama.

```Python
def get_feature_reps(x, layer_names, model):
    featMatrices = []
    for ln in layer_names:
        selectedLayer = model.get_layer(ln)
        featRaw = selectedLayer.output
        featRawShape = K.shape(featRaw).eval(session=tf_session)
        N_l = featRawShape[-1]
        M_l = featRawShape[1]*featRawShape[2]
        featMatrix = K.reshape(featRaw, (M_l, N_l))
        featMatrix = K.transpose(featMatrix)
        featMatrices.append(featMatrix)
    return featMatrices

def get_content_loss(F, P):
    cLoss = 0.5*K.sum(K.square(F - P))
    return cLoss
'''
Gram Matrix
'''
def get_Gram_matrix(F):
    G = K.dot(F, K.transpose(F))
    return G

def get_style_loss(ws, Gs, As):
    sLoss = K.variable(0.)
    for w, G, A in zip(ws, Gs, As):
        M_l = K.int_shape(G)[1]
        N_l = K.int_shape(G)[0]
        G_gram = get_Gram_matrix(G)
        A_gram = get_Gram_matrix(A)
        sLoss.assign_add(w*0.25*K.sum(K.square(G_gram - A_gram))/ (N_l**2 * M_l**2))
    return sLoss
```

Łączymy wszystkie funkcje stratne w jedna główna funkcje

```Python
def get_total_loss(gImPlaceholder, alpha=1.0, beta=10000.0):
    F = get_feature_reps(gImPlaceholder, layer_names=[cLayerName], model=gModel)[0]
    Gs = get_feature_reps(gImPlaceholder, layer_names=sLayerNames, model=gModel)
    contentLoss = get_content_loss(F, P)
    styleLoss = get_style_loss(ws, Gs, As)
    totalLoss = alpha*contentLoss + beta*styleLoss
    return totalLoss
```
Obliczanie całkowitej straty która odzwierdziela nam stracone macierze podczas wykonywania sie skryptu. Te macierze umożliwiają nam podobieństwo obrazu wyjściowego z obrazem bazowym.

```Python

def calculate_loss(gImArr):

    if gImArr.shape != (1, targetWidth, targetWidth, 3):
        gImArr = gImArr.reshape((1, targetWidth, targetHeight, 3))
    loss_fcn = K.function([gModel.input], [get_total_loss(gModel.input)])
    return loss_fcn([gImArr])[0].astype('float64')
```
Funkcja gradient wygładza łączone krawędzie obrazu

```Python
def get_grad(gImArr):

    if gImArr.shape != (1, targetWidth, targetHeight, 3):
        gImArr = gImArr.reshape((1, targetWidth, targetHeight, 3))
    grad_fcn = K.function([gModel.input], K.gradients(get_total_loss(gModel.input), [gModel.input]))
    grad = grad_fcn([gImArr])[0].flatten().astype('float64')
    return grad
```

Zaczynamy interpretować kod. Wykorzystujemy do tego architekture z TensorFlow Backend VGG16 która tworzy 16 warstw. Obraz jest dzielony na 16 warstw i na każdej warstwie, są iterowane. 

![](https://miro.medium.com/max/470/1*3-TqqkRQ4rWLOMX-gvkYwA.png)

```Python
def postprocess_array(x):

    if x.shape != (targetWidth, targetHeight, 3):
        x = x.reshape((targetWidth, targetHeight, 3))
    x[..., 0] += 103.939
    x[..., 1] += 116.779
    x[..., 2] += 123.68
    x = x[..., ::-1]
    x = np.clip(x, 0, 255)
    x = x.astype('uint8')
    return x

def reprocess_array(x):
    x = np.expand_dims(x.astype('float64'), axis=0)
    x = preprocess_input(x)
    return x

def save_original_size(x, target_size=cImageSizeOrig):
    xIm = Image.fromarray(x)
    xIm = xIm.resize(target_size)
    xIm.save(genImOutputPath)
    return xIm

tf_session = K.get_session()
cModel = VGG16(include_top=False, weights='imagenet', input_tensor=cImArr)
sModel = VGG16(include_top=False, weights='imagenet', input_tensor=sImArr)
gModel = VGG16(include_top=False, weights='imagenet', input_tensor=gImPlaceholder)
cLayerName = 'block4_conv2'
sLayerNames = [
                'block1_conv1',
                'block2_conv1',
                'block3_conv1',
                'block4_conv1',
                ]

P = get_feature_reps(x=cImArr, layer_names=[cLayerName], model=cModel)[0]
As = get_feature_reps(x=sImArr, layer_names=sLayerNames, model=sModel)
ws = np.ones(len(sLayerNames))/float(len(sLayerNames))
```
Trzeba wybra liczbe iteracji. Optymalna ilość iteracji to pomiędzy 500, a 600, ale wymagaja one dobrych podzespołów. Nam udało sie uzyskać wyniki z 100 i 200 iteracjiami i też uważamy, że są całkiem niezłe. Implementujemy również informowanie o danym stanie iteracjii.

```Python
iterations = 500
x_val = gIm0.flatten()
start = time.time()
xopt, f_val, info= fmin_l_bfgs_b(calculate_loss, x_val, fprime=get_grad,
                            maxiter=iterations, disp=True)
xOut = postprocess_array(xopt)
xIm = save_original_size(xOut)
```
Na końcu zapisujemy wynik

```Python
print('Image saved')
end = time.time()
print('Time taken: {}'.format(end-start))
```
##A oto co uzyskaliśmy

####Obraz bazowy

![](https://github.com/kacperkaczor97/narzedzia_sztucznej_inteligencji/blob/master/AiArtGenerator/base_image.jpg?raw=true)

####Obraz wzorcowy

![](https://github.com/kacperkaczor97/narzedzia_sztucznej_inteligencji/blob/master/AiArtGenerator/reference_image.jpg?raw=true)

####Nasze wyniki
100 Iteracji
![](https://github.com/kacperkaczor97/narzedzia_sztucznej_inteligencji/blob/master/AiArtGenerator/output100.jpg?raw=true)

200 Iteracji
![](https://github.com/kacperkaczor97/narzedzia_sztucznej_inteligencji/blob/master/AiArtGenerator/output200.jpg?raw=true)

#Koniec