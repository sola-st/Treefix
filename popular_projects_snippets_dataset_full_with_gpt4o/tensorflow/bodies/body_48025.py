# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if self._graph_initialized:
    self._init_graph_network(self.inputs, self.outputs)
else:
    if input_shape is None:
        raise ValueError('You must provide an `input_shape` argument.')
    self._build_graph_network_for_inferred_shape(input_shape)
    if not self.built:
        input_shape = tuple(input_shape)
        self._build_input_shape = input_shape
        super(Sequential, self).build(input_shape)
self.built = True
