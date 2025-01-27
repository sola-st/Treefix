# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if inputs_shape[-1] is None:
    raise ValueError("Expected inputs.shape[-1] to be known, saw shape: %s" %
                     str(inputs_shape))
_check_supported_dtypes(self.dtype)
input_depth = inputs_shape[-1]
h_depth = self._num_units
self._kernel = self.add_variable(
    _WEIGHTS_VARIABLE_NAME,
    shape=[input_depth + h_depth, 4 * self._num_units])
self._bias = self.add_variable(
    _BIAS_VARIABLE_NAME,
    shape=[4 * self._num_units],
    initializer=init_ops.zeros_initializer(dtype=self.dtype))

self.built = True
