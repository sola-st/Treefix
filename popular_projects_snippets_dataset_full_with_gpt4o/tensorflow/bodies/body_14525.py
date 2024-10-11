# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
"""Adds additional NumPy methods on tf.Tensor class."""
t = property(_tensor_t)
setattr(ops.Tensor, 'T', t)

ndim = property(_tensor_ndim)
setattr(ops.Tensor, 'ndim', ndim)

size = property(_tensor_size)
setattr(ops.Tensor, 'size', size)

setattr(ops.Tensor, '__pos__', _tensor_pos)
setattr(ops.Tensor, 'tolist', _tensor_tolist)

# TODO(b/178540516): Make a custom `setattr` that changes the method's
#   docstring to the TF one.
setattr(ops.Tensor, 'transpose', np_array_ops.transpose)
setattr(ops.Tensor, 'reshape', np_array_ops._reshape_method_wrapper)  # pylint: disable=protected-access
setattr(ops.Tensor, 'ravel', np_array_ops.ravel)
setattr(ops.Tensor, 'clip', clip)
setattr(ops.Tensor, 'astype', math_ops.cast)
setattr(ops.Tensor, '__round__', np_array_ops.around)
setattr(ops.Tensor, 'max', np_array_ops.amax)
setattr(ops.Tensor, 'mean', np_array_ops.mean)
setattr(ops.Tensor, 'min', np_array_ops.amin)

# TODO(wangpeng): Remove `data` when all uses of it are removed
data = property(lambda self: self)
setattr(ops.Tensor, 'data', data)
