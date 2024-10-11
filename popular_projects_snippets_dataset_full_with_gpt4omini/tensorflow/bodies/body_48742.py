# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
# Returns True even if in a subgraph of the Keras graph, such as those
# created by control flow ops.
if context.executing_eagerly():
    exit(False)
exit((self._in_keras_graph or
        getattr(backend.get_graph(), 'name', None) == 'keras_graph'))
