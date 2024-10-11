# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Initialize the parameters for an LSTM cell.

    Args:
      num_units: int, The number of units in the LSTM cell.
      use_peepholes: bool, set True to enable diagonal/peephole connections.
      cell_clip: (optional) A float value, if provided the cell state is clipped
        by this value prior to the cell output activation.
      initializer: (optional) The initializer to use for the weight and
        projection matrices.
      num_proj: (optional) int, The output dimensionality for the projection
        matrices.  If None, no projection is performed.
      proj_clip: (optional) A float value.  If `num_proj > 0` and `proj_clip` is
        provided, then the projected values are clipped elementwise to within
        `[-proj_clip, proj_clip]`.
      num_unit_shards: Deprecated, will be removed by Jan. 2017. Use a
        variable_scope partitioner instead.
      num_proj_shards: Deprecated, will be removed by Jan. 2017. Use a
        variable_scope partitioner instead.
      forget_bias: Biases of the forget gate are initialized by default to 1 in
        order to reduce the scale of forgetting at the beginning of the
        training. Must set it manually to `0.0` when restoring from CudnnLSTM
        trained checkpoints.
      state_is_tuple: If True, accepted and returned states are 2-tuples of the
        `c_state` and `m_state`.  If False, they are concatenated along the
        column axis.  This latter behavior will soon be deprecated.
      activation: Activation function of the inner states.  Default: `tanh`. It
        could also be string that is within Keras activation function names.
      reuse: (optional) Python boolean describing whether to reuse variables in
        an existing scope.  If not `True`, and the existing scope already has
        the given variables, an error is raised.
      name: String, the name of the layer. Layers with the same name will share
        weights, but to avoid mistakes we require reuse=True in such cases.
      dtype: Default dtype of the layer (default of `None` means use the type of
        the first input). Required when `build` is called before `call`.
      **kwargs: Dict, keyword named properties for common layer attributes, like
        `trainable` etc when constructing the cell from configs of get_config().
        When restoring from CudnnLSTM-trained checkpoints, use
        `CudnnCompatibleLSTMCell` instead.
    """
warnings.warn("`tf.nn.rnn_cell.LSTMCell` is deprecated and will be "
              "removed in a future version. This class "
              "is equivalent as `tf.keras.layers.LSTMCell`, "
              "and will be replaced by that in Tensorflow 2.0.")
super(LSTMCell, self).__init__(
    _reuse=reuse, name=name, dtype=dtype, **kwargs)
_check_supported_dtypes(self.dtype)
if not state_is_tuple:
    logging.warning(
        "%s: Using a concatenated state is slower and will soon be "
        "deprecated.  Use state_is_tuple=True.", self)
if num_unit_shards is not None or num_proj_shards is not None:
    logging.warning(
        "%s: The num_unit_shards and proj_unit_shards parameters are "
        "deprecated and will be removed in Jan 2017.  "
        "Use a variable scope with a partitioner instead.", self)
if context.executing_eagerly() and tf_config.list_logical_devices("GPU"):
    logging.warning(
        "%s: Note that this cell is not optimized for performance. "
        "Please use tf.contrib.cudnn_rnn.CudnnLSTM for better "
        "performance on GPU.", self)

# Inputs must be 2-dimensional.
self.input_spec = input_spec.InputSpec(ndim=2)

self._num_units = num_units
self._use_peepholes = use_peepholes
self._cell_clip = cell_clip
self._initializer = initializers.get(initializer)
self._num_proj = num_proj
self._proj_clip = proj_clip
self._num_unit_shards = num_unit_shards
self._num_proj_shards = num_proj_shards
self._forget_bias = forget_bias
self._state_is_tuple = state_is_tuple
if activation:
    self._activation = activations.get(activation)
else:
    self._activation = math_ops.tanh

if num_proj:
    self._state_size = (
        LSTMStateTuple(num_units, num_proj) if state_is_tuple else num_units +
        num_proj)
    self._output_size = num_proj
else:
    self._state_size = (
        LSTMStateTuple(num_units, num_units) if state_is_tuple else 2 *
        num_units)
    self._output_size = num_units
