# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Initialize the basic LSTM cell.

    Args:
      num_units: int, The number of units in the LSTM cell.
      forget_bias: float, The bias added to forget gates (see above). Must set
        to `0.0` manually when restoring from CudnnLSTM-trained checkpoints.
      state_is_tuple: If True, accepted and returned states are 2-tuples of the
        `c_state` and `m_state`.  If False, they are concatenated along the
        column axis.  The latter behavior will soon be deprecated.
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
        When restoring from CudnnLSTM-trained checkpoints, must use
        `CudnnCompatibleLSTMCell` instead.
    """
warnings.warn("`tf.nn.rnn_cell.BasicLSTMCell` is deprecated and will be "
              "removed in a future version. This class "
              "is equivalent as `tf.keras.layers.LSTMCell`, "
              "and will be replaced by that in Tensorflow 2.0.")
super(BasicLSTMCell, self).__init__(
    _reuse=reuse, name=name, dtype=dtype, **kwargs)
_check_supported_dtypes(self.dtype)
if not state_is_tuple:
    logging.warning(
        "%s: Using a concatenated state is slower and will soon be "
        "deprecated.  Use state_is_tuple=True.", self)
if context.executing_eagerly() and tf_config.list_logical_devices("GPU"):
    logging.warning(
        "%s: Note that this cell is not optimized for performance. "
        "Please use tf.contrib.cudnn_rnn.CudnnLSTM for better "
        "performance on GPU.", self)

# Inputs must be 2-dimensional.
self.input_spec = input_spec.InputSpec(ndim=2)

self._num_units = num_units
self._forget_bias = forget_bias
self._state_is_tuple = state_is_tuple
if activation:
    self._activation = activations.get(activation)
else:
    self._activation = math_ops.tanh
