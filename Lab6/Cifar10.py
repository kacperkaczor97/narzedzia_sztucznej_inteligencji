# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

cifar10 = tf.keras.datasets.cifar10

# (train_images, train_labels), (test_images, test_labels)
(x_train, y_train), (x_test, y_test)= cifar10.load_data()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']


# reshaping
x_train = x_train.reshape(x_train.shape[0], 32, 32, 3)
x_test = x_test.reshape(y_test.shape[0], 32, 32, 3)

# define the model
model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32,32,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
        ])

model.compile(optimizer='adam', loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

# train
model.fit(x_train, y_train, epochs=10)
test_loss, test_acc = model.evaluate(x_train, y_train, verbose=2)

print("Test accuracy: ", test_acc)