'''
Autorzy:
Karol Niemykin
Kacper Kaczor

Celem zadania jest nauczy program rozpoznawania zwierzat poprzez siec neuronowa ze zbioru CIFAR-10

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
cifar10 = tf.keras.datasets.cifar10

# (train_images, train_labels), (test_images, test_labels)
(x_train, y_train), (x_test, y_test)= cifar10.load_data()
'''
Przypisanie etykiet do obrazkow
'''
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']


'''
Przeksztalcenie formatow obrazkow
'''
x_train = x_train.reshape(x_train.shape[0], 32, 32, 3)
x_test = x_test.reshape(y_test.shape[0], 32, 32, 3)

'''
Definiowanie modelu do konstruktora 2D
'''
model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32,32,3)),
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
