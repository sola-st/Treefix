# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
self._trainable = value
for layer in getattr(self, '_self_tracked_trackables', []):
    layer.trainable = value
