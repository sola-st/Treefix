# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if inputs_shape[-1] is None:
    raise ValueError("Expected inputs.shape[-1] to be known, saw shape: %s" %
                     str(inputs_shape))
_check_supported_dtypes(self.dtype)
input_depth = inputs_shape[-1]
h_depth = self._num_units if self._num_proj is None else self._num_proj
maybe_partitioner = (
    partitioned_variables.fixed_size_partitioner(self._num_unit_shards)
    if self._num_unit_shards is not None else None)
self._kernel = self.add_variable(
    _WEIGHTS_VARIABLE_NAME,
    shape=[input_depth + h_depth, 4 * self._num_units],
    initializer=self._initializer,
    partitioner=maybe_partitioner)
if self.dtype is None:
    initializer = init_ops.zeros_initializer
else:
    initializer = init_ops.zeros_initializer(dtype=self.dtype)
self._bias = self.add_variable(
    _BIAS_VARIABLE_NAME,
    shape=[4 * self._num_units],
    initializer=initializer)
if self._use_peepholes:
    self._w_f_diag = self.add_variable(
        "w_f_diag", shape=[self._num_units], initializer=self._initializer)
    self._w_i_diag = self.add_variable(
        "w_i_diag", shape=[self._num_units], initializer=self._initializer)
    self._w_o_diag = self.add_variable(
        "w_o_diag", shape=[self._num_units], initializer=self._initializer)

if self._num_proj is not None:
    maybe_proj_partitioner = (
        partitioned_variables.fixed_size_partitioner(self._num_proj_shards)
        if self._num_proj_shards is not None else None)
    self._proj_kernel = self.add_variable(
        "projection/%s" % _WEIGHTS_VARIABLE_NAME,
        shape=[self._num_units, self._num_proj],
        initializer=self._initializer,
        partitioner=maybe_proj_partitioner)

self.built = True
