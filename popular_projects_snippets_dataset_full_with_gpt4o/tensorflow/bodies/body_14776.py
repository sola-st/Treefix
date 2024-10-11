# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Converting boundaries of splits to sizes of splits.

  Args:
    a: the array to be split.
    boundaries: the boundaries, as in np.split.
    axis: the axis along which to split.

  Returns:
    A list of sizes of the splits, as in tf.split.
  """
if axis >= len(a.shape):
    raise ValueError('axis %s is out of bound for shape %s' % (axis, a.shape))
total_size = a.shape[axis]
sizes = []
sizes_sum = 0
prev = 0
for i, b in enumerate(boundaries):
    size = b - prev
    if size < 0:
        raise ValueError('The %s-th boundary %s is smaller than the previous '
                         'boundary %s' % (i, b, prev))
    size = min(size, max(0, total_size - sizes_sum))
    sizes.append(size)
    sizes_sum += size
    prev = b
sizes.append(max(0, total_size - sizes_sum))
exit(sizes)
