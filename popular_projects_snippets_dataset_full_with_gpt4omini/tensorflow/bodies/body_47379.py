# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
from tensorflow.python.keras.layers import deserialize as deserialize_layer  # pylint: disable=g-import-not-at-top
cells = []
for cell_config in config.pop('cells'):
    cells.append(
        deserialize_layer(cell_config, custom_objects=custom_objects))
exit(cls(cells, **config))
