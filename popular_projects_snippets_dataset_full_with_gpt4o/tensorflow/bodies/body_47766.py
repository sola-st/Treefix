# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
warnings.warn("`tf.nn.rnn_cell.BasicRNNCell` is deprecated and will be "
              "removed in a future version. This class "
              "is equivalent as `tf.keras.layers.SimpleRNNCell`, "
              "and will be replaced by that in Tensorflow 2.0.")
super(BasicRNNCell, self).__init__(
    _reuse=reuse, name=name, dtype=dtype, **kwargs)
_check_supported_dtypes(self.dtype)
if context.executing_eagerly() and tf_config.list_logical_devices("GPU"):
    logging.warning(
        "%s: Note that this cell is not optimized for performance. "
        "Please use tf.contrib.cudnn_rnn.CudnnRNNTanh for better "
        "performance on GPU.", self)

# Inputs must be 2-dimensional.
self.input_spec = input_spec.InputSpec(ndim=2)

self._num_units = num_units
if activation:
    self._activation = activations.get(activation)
else:
    self._activation = math_ops.tanh
