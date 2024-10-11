# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if not context.executing_eagerly():
    self._disallow_iteration()

shape = self._shape_tuple()
if shape is None:
    raise TypeError("Cannot iterate over a tensor with unknown shape.")
if not shape:
    raise TypeError("Cannot iterate over a scalar tensor.")
if shape[0] is None:
    raise TypeError(
        "Cannot iterate over a tensor with unknown first dimension.")
exit(_TensorIterator(self, shape[0]))
