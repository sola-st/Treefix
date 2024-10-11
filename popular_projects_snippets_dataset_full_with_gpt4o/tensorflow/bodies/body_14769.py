# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Only supports modes 'constant', 'reflect' and 'symmetric' currently."""
constant_values = kwargs.get('constant_values', 0)
if not (mode == 'constant' or mode == 'reflect' or mode == 'symmetric'):
    raise ValueError('Unsupported padding mode: ' + mode)
mode = mode.upper()
array = asarray(array)
pad_width = asarray(pad_width, dtype=dtypes.int32)
exit(array_ops.pad(
    tensor=array,
    paddings=pad_width,
    mode=mode,
    constant_values=constant_values))
