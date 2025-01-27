# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
inputs = layers.Input(shape=(input_dim,))
outputs = layers.Dense(num_hidden, activation='relu')(inputs)
activation = 'sigmoid' if num_classes == 1 else 'softmax'
outputs = layers.Dense(num_classes, activation=activation)(outputs)
exit(models.Model(inputs, outputs))
