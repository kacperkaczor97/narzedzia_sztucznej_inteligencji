'''
Autorzy:
Karol Niemykin
Kacper Kaczor
Celem zadania jest nauczy program rozpoznawania liczb poprzez siec neuronowa ze zbioru Mnist
Uruchomienie:
  - Pobrac projekt z Github
  - Stworzyc projekt w PyCharm
  - Zimportowac biblioteki i uruchomic program
'''

'''
Importowanie potrzebnych bibliotek
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
'''
Importowanie danych z biblioteki TensorFlow
'''
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test)= mnist.load_data()
'''
Przypisanie etykiet do obrazkow
'''
class_names = ['0', '1', '2', '3', '4',
               '5', '6', '7', '8', '9']

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[y_train[i]])
plt.show()

'''
Przeksztalcenie formatow obrazkow
'''
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(y_test.shape[0], 28, 28, 1)
'''
Definiowanie modelu do konstruktora 2D
'''
model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
        ])
'''
Kompilacja i optymalizacja modelu
'''
model.compile(optimizer='adam', loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

'''
Wytrenowanie modelu
'''
model.fit(x_train, y_train, epochs=10)
test_loss, test_acc = model.evaluate(x_train, y_train, verbose=2)
'''
Wypisanie dokladnosci uczenia
'''
print("Test accuracy: ", test_acc)
