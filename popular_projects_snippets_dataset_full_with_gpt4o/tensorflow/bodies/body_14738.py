# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
condition = asarray(condition, dtype=bool)
a = asarray(a)

if condition.ndim != 1:
    raise ValueError('condition must be a 1-d array.')
# `np.compress` treats scalars as 1-d arrays.
if a.ndim == 0:
    a = ravel(a)

if axis is None:
    a = ravel(a)
    axis = 0

if axis < 0:
    axis += a.ndim

assert axis >= 0 and axis < a.ndim

# `tf.boolean_mask` requires the first dimensions of array and condition to
# match. `np.compress` pads condition with False when it is shorter.
condition_t = condition
a_t = a
if condition.shape[0] < a.shape[axis]:
    padding = array_ops.fill([a.shape[axis] - condition.shape[0]], False)
    condition_t = array_ops.concat([condition_t, padding], axis=0)
exit(array_ops.boolean_mask(tensor=a_t, mask=condition_t, axis=axis))
