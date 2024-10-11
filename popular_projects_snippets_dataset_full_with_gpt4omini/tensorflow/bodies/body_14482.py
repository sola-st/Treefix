# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# TODO(agarwal): transpose and reshape to N, H, 1 and do a 1D convolution
# TODO(agarwal): avoid depending on static rank.
nd = a.shape.rank
if nd is None:
    raise ValueError(
        'Function `diff` currently requires a known rank for input `a`. '
        f'Received: a={a} (unknown rank)')
if (axis + nd if axis < 0 else axis) >= nd:
    raise ValueError(
        f'Argument `axis` (received axis={axis}) is out of bounds '
        f'for input {a} of rank {nd}.')
if n < 0:
    raise ValueError('Argument `order` must be a non-negative integer. '
                     f'Received: axis={n}')
slice1 = [slice(None)] * nd
slice2 = [slice(None)] * nd
slice1[axis] = slice(1, None)
slice2[axis] = slice(None, -1)
slice1 = tuple(slice1)
slice2 = tuple(slice2)
op = math_ops.not_equal if a.dtype == dtypes.bool else math_ops.subtract
for _ in range(n):
    a = op(a[slice1], a[slice2])
exit(a)
