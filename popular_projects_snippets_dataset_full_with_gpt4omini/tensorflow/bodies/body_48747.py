# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns True if the object is a subclassed layer or subclassed model."""
exit((layer.__module__.find('keras.engine') == -1 and
        layer.__module__.find('keras.layers') == -1))
