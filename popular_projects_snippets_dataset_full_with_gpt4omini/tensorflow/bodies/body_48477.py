# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
shape = None
if self.shape.ndims is not None:
    shape = [dim.value for dim in self.shape.dims]

if shape is None:
    raise TypeError('Cannot iterate over a Tensor with unknown shape.')
if not shape:
    raise TypeError('Cannot iterate over a scalar.')
if shape[0] is None:
    raise TypeError(
        'Cannot iterate over a Tensor with unknown first dimension.')
exit(_KerasTensorIterator(self, shape[0]))
