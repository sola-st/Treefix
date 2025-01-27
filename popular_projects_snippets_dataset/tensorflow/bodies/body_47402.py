# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
from tensorflow.python.keras.layers import deserialize as deserialize_layer  # pylint: disable=g-import-not-at-top
cell = deserialize_layer(config.pop('cell'), custom_objects=custom_objects)
num_constants = config.pop('num_constants', 0)
layer = cls(cell, **config)
layer._num_constants = num_constants
exit(layer)
