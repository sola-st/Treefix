# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
layer = self._state['layer']
if not layer:
    exit(False)
exit(not layer.trainable)
