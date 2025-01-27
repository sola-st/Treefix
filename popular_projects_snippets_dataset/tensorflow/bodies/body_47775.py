# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if inputs_shape[-1] is None:
    raise ValueError("Expected inputs.shape[-1] to be known, saw shape: %s" %
                     str(inputs_shape))
_check_supported_dtypes(self.dtype)
input_depth = inputs_shape[-1]
self._gate_kernel = self.add_variable(
    "gates/%s" % _WEIGHTS_VARIABLE_NAME,
    shape=[input_depth + self._num_units, 2 * self._num_units],
    initializer=self._kernel_initializer)
self._gate_bias = self.add_variable(
    "gates/%s" % _BIAS_VARIABLE_NAME,
    shape=[2 * self._num_units],
    initializer=(self._bias_initializer
                 if self._bias_initializer is not None else
                 init_ops.constant_initializer(1.0, dtype=self.dtype)))
self._candidate_kernel = self.add_variable(
    "candidate/%s" % _WEIGHTS_VARIABLE_NAME,
    shape=[input_depth + self._num_units, self._num_units],
    initializer=self._kernel_initializer)
self._candidate_bias = self.add_variable(
    "candidate/%s" % _BIAS_VARIABLE_NAME,
    shape=[self._num_units],
    initializer=(self._bias_initializer
                 if self._bias_initializer is not None else
                 init_ops.zeros_initializer(dtype=self.dtype)))

self.built = True
