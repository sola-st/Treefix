# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_spec.py
self.dtype = dtypes.as_dtype(dtype).name if dtype is not None else None
shape = tensor_shape.TensorShape(shape)
if shape.rank is None:
    shape = None
else:
    shape = tuple(shape.as_list())
if shape is not None:
    self.ndim = len(shape)
    self.shape = shape
else:
    self.ndim = ndim
    self.shape = None
self.max_ndim = max_ndim
self.min_ndim = min_ndim
self.name = name
self.allow_last_axis_squeeze = allow_last_axis_squeeze
try:
    axes = axes or {}
    self.axes = {int(k): axes[k] for k in axes}
except (ValueError, TypeError):
    raise TypeError('The keys in axes must be integers.')

if self.axes and (self.ndim is not None or self.max_ndim is not None):
    max_dim = (self.ndim if self.ndim else self.max_ndim) - 1
    max_axis = max(self.axes)
    if max_axis > max_dim:
        raise ValueError('Axis {} is greater than the maximum allowed value: {}'
                         .format(max_axis, max_dim))
