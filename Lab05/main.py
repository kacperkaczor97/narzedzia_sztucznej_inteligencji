'''
Autorzy:
Karol Niemykin
Kacper Kaczor

Celem zadania jest nauczyć nasz program rozpoznawania jakości białego wina.

- Pobrać plik main.py i winequality-white.csv z gita
- Stworzyć nowy projekt w PyCharm
- Dodać plik main.py, winequality-white.csv i uruchomić program
'''

'''
Importujemy przydatne biblioteki
'''
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

'''
Wczytywanie pliku csv z informacjami o białych winach
'''
wine = pd.read_csv('winequality-white.csv', sep=';')

'''
Zastępujemy wartości ostatniej kolumny "quality" wartościami 1 i 0
dla win z jakością 1-5.9 = 0 - złe wino
dla win z jakością 6-10  = 1 - dobre wino
'''
bins = (1, 6, 10)
group_names = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins=bins, labels=group_names)
label_quality = LabelEncoder()
wine['quality'] = label_quality.fit_transform(wine['quality'])

'''
Wyświetlamy ilość dobrych i złych win
'''
print("Jakość win w bazie: \n", wine['quality'].value_counts())

'''
Deklarujemy zmienną odpowiedzialną i funkcyjną i rozpoczynamy naukę naszego programu
'''
X = wine.drop('quality', axis=1)
y = wine['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

'''
Zastosowaliśmy standardowe skalowania w celu uzyskania opytymalnego wyniku
'''
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

'''
Wykorzystujemy Support Vector Classifier w celu rozróżnienia dobrego wina od złego
'''
clf = svm.SVC()
clf.fit(X_train, y_train)
pred_clf = clf.predict(X_test)
'''
Sprawdzamy działanie za pomocą poniższych przykładów dla Xinput: 
#1 good wine case: [[6.6, 0.16, 0.40, 1.50, 0.044, 48.0, 143.0, 0.9912, 3.54, 0.52, 12.4]]
#2 bad wine case: [[7.3, 0.58, 0.00, 1.8, 0.065, 15.0, 21.0, 0.9946, 3.36, 0.45, 9.1]]
#3 bad wine case: [[7.8, 0.58, 0.01, 2.0, 0.073, 9.0, 17.0, 0.9968, 3.36, 0.57, 9.4]]
'''
Xinput = [[7.8, 0.58, 0.01, 2.0, 0.073, 9.0, 17.0, 0.9968, 3.36, 0.57, 9.4]]
print(Xinput)
Xinput = sc.transform(Xinput)
yinput = clf.predict(Xinput)

if yinput == [0]:
    print("To wino jest złe")
else:
    print("To wino jest dobre")

