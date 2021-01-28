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
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
'''
Przypisanie etykiet do obrazkow
'''
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

'''
Przeksztalcenie formatow obrazkow
'''
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

'''
Przeksztalcenie formatow obrazkow
'''
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

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
model.fit(train_images, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(train_images, train_labels, verbose=2)
'''
Wypisanie dokladnosci uczenia
'''
print("Test accuracy: ", test_acc)
