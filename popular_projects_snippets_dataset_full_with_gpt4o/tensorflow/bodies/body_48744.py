# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
call_ctx = self._call_ctx
self._prev_in_call = call_ctx.in_call
self._prev_state = call_ctx._state

call_ctx.in_call = True
call_ctx._state = self._state

# TODO(b/150169018): This logic can be removed after the Functional API
# refactor.
if self._build_graph:
    self._prev_in_keras_graph = call_ctx._in_keras_graph
    call_ctx._in_keras_graph = (
        call_ctx._in_keras_graph or
        getattr(backend.get_graph(), 'name', None) == 'keras_graph')
