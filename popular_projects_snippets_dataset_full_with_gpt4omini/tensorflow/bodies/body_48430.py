# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
data = next(iterator)
self._adapt_maybe_build(data)
self.update_state(data)
