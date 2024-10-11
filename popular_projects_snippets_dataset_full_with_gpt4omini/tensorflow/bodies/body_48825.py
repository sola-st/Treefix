# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
for layer in self.layers:
    if hasattr(layer, 'reset_states') and getattr(layer, 'stateful', False):
        layer.reset_states()
