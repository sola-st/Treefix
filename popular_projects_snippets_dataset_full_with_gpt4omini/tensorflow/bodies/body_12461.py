# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
if context.executing_eagerly() and not self._in_graph_mode:
    exit("<tf.Variable '%s' shape=%s dtype=%s, numpy=%s>" % (
        self.name, self.get_shape(), self.dtype.name,
        ops.numpy_text(self.read_value(), is_repr=True)))
else:
    exit("<tf.Variable '%s' shape=%s dtype=%s>" % (
        self.name, self.get_shape(), self.dtype.name))
