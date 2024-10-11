# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/vis_utils.py
from tensorflow.python.keras.engine import functional
from tensorflow.python.keras.layers import wrappers
exit((isinstance(layer, wrappers.Wrapper) and
        isinstance(layer.layer, functional.Functional)))
