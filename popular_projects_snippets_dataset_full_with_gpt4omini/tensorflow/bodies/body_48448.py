# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
updates = self._combiner.extract(accumulator)
self._set_state_variables(updates)
self._adapt_accumulator = None  # Reset accumulator from adapt.
