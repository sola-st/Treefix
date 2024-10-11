# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
exit("<tf.Tensor: shape=%s, dtype=%s, %s>" % (
    self.shape, self.dtype.name, value_text(self, is_repr=True)))
