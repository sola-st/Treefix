# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
# Handle `in_call` separately as it is the most-read attr and reading it is
# on the hot path.
self.in_call = False
self._state = {
    'layer': None,
    'inputs': None,
    'build_graph': False,
    'training': None,
    'saving': None
}
# TODO(b/150169018): This logic can be replaced after the Functional API
# refactor.
self._in_keras_graph = False
