# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Removes the last layer in the model.

    Raises:
        TypeError: if there are no layers in the model.
    """
if not self.layers:
    raise TypeError('There are no layers in the model.')

layer = self._self_tracked_trackables.pop()
self._layer_call_argspecs.pop(layer)
if not self.layers:
    self.outputs = None
    self.inputs = None
    self.built = False
    self._inferred_input_shape = None
    self._has_explicit_input_shape = False
    self._graph_initialized = False
elif self._graph_initialized:
    self.layers[-1]._outbound_nodes = []
    self.outputs = [self.layers[-1].output]
    self._init_graph_network(self.inputs, self.outputs)
    self.built = True
