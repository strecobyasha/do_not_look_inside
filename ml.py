import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras.datasets import mnist
from keras.optimizers import Adam

tf.config.list_physical_devices('GPU')


class Digits:

    def __init__(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.model = None

    def prepare_data(self):
        self.x_train = self.x_train.reshape(self.x_train.shape + (1,))
        self.x_test = self.x_test.reshape(self.x_test.shape + (1,))

        self.x_train = self.x_train / 255.
        self.x_test = self.x_test / 255.

        self.x_train = self.x_train.astype(np.float32)
        self.x_test = self.x_test.astype(np.float32)

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=Adam(learning_rate=0.001),
            metrics=['accuracy'],
        )
        self.model.fit(self.x_train, self.y_train, epochs=12)

        return self.model

    def test_model(self, model):
        predictions = model.predict(self.x_test)
        for i in range(3):
            plt.figure(figsize=(3, 3))
            plt.imshow(self.x_test[i], cmap='gray')
            plt.title(f'{self.y_test[i]}, {np.argmax(predictions[i])}')
            plt.axis(False)
            plt.show()


if __name__ == '__main__':
    digits = Digits()
    digits.prepare_data()
    model = digits.create_model()
    digits.test_model(model)
