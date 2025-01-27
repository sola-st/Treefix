# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if self._saved_model_inputs_spec is None:
    exit(None)

exit(nest.map_structure(
    lambda t: tf_utils.get_tensor_spec(t, dynamic_batch=dynamic_batch),
    self._saved_model_inputs_spec))
