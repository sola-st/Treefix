# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
exit(all(hasattr(x, '_keras_history') for x in nest.flatten(tensors)))
