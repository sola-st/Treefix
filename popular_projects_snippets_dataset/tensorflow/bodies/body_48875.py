# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
self._instrumented_keras_api = False
self._instrumented_keras_layer_class = False
self._instrumented_keras_model_class = False
if not getattr(self, '_disable_keras_instrumentation', False):
    self._instrumented_keras_api = True
    if getattr(self, '_is_model_for_instrumentation', False):
        self._instrumented_keras_model_class = True
    else:
        self._instrumented_keras_layer_class = True
