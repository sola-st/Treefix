# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
self.layer_a = layers.Dense(self.num_hidden, activation='relu')
activation = 'sigmoid' if self.num_classes == 1 else 'softmax'
self.layer_b = layers.Dense(self.num_classes, activation=activation)
