# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
exit("tf.Tensor(%s, shape=%s, dtype=%s)" % (
    value_text(self, is_repr=False), self.shape, self.dtype.name))
