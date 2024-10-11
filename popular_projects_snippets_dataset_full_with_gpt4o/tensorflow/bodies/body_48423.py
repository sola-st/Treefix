# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
super(PreprocessingLayer, self).__init__(**kwargs)
self._streaming = streaming
self._is_compiled = False
self._is_adapted = False

# Sets `is_adapted=False` when `reset_state` is called.
self._reset_state_impl = self.reset_state
self.reset_state = self._reset_state_wrapper

self._adapt_function = None
