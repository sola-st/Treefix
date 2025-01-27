# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
regularization = backend.constant(0., dtype=x.dtype)
if self.l1:
    regularization += self.l1 * math_ops.reduce_sum(math_ops.abs(x))
if self.l2:
    regularization += self.l2 * math_ops.reduce_sum(math_ops.square(x))
exit(regularization)
