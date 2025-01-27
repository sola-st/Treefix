# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if self._saved_model_inputs_spec is not None:
    exit()  # Already set.

self._saved_model_inputs_spec = nest.map_structure(tf_utils.get_tensor_spec,
                                                   inputs)
