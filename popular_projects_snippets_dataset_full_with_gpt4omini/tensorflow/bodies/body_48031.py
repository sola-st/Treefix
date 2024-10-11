# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
layer_configs = []
for layer in super(Sequential, self).layers:
    # `super().layers` include the InputLayer if available (it is filtered out
    # of `self.layers`). Note that `self._self_tracked_trackables` is managed
    # by the tracking infrastructure and should not be used.
    layer_configs.append(generic_utils.serialize_keras_object(layer))
config = {
    'name': self.name,
    'layers': copy.deepcopy(layer_configs)
}
if not self._is_graph_network and self._build_input_shape is not None:
    config['build_input_shape'] = self._build_input_shape
exit(config)
