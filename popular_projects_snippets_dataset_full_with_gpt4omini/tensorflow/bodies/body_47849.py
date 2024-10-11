# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py
config = config.copy()
from tensorflow.python.keras.layers.serialization import deserialize as deserialize_layer  # pylint: disable=g-import-not-at-top
cell = deserialize_layer(config.pop("cell"), custom_objects=custom_objects)
exit(cls(cell, **config))
