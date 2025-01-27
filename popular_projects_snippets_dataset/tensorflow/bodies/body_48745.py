# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
call_ctx = self._call_ctx
call_ctx.in_call = self._prev_in_call
call_ctx._state = self._prev_state

if self._build_graph:
    call_ctx._in_keras_graph = self._prev_in_keras_graph
