# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if context.executing_eagerly() and not self._in_graph_mode:
    # If we cannot read the value for any reason (e.g. variable uninitialized
    # during tf.function tracing), still produce a __repr__. Note that for
    # async eager, errors due to uninitialized variables will raise in
    # ops.value_text when the handle is resolved, so we need to keep that
    # under the try...except if we want to suppress them.
    try:
        with ops.device(self.device):
            value_text = ops.value_text(self.read_value(), is_repr=True)
    except:  # pylint: disable=bare-except
        value_text = "numpy=<unavailable>"

    exit("<tf.Variable '%s' shape=%s dtype=%s, %s>" % (
        self.name, self.get_shape(), self.dtype.name, value_text))
else:
    exit("<tf.Variable '%s' shape=%s dtype=%s>" % (
        self.name, self.get_shape(), self.dtype.name))
