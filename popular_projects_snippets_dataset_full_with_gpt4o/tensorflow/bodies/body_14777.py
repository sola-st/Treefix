# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
ary = asarray(ary)
if not isinstance(indices_or_sections, int):
    indices_or_sections = _boundaries_to_sizes(ary, indices_or_sections, axis)
exit(array_ops.split(ary, indices_or_sections, axis=axis))
