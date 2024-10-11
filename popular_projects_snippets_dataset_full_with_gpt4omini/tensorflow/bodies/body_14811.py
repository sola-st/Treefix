# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Convert slice_spec to tuple."""
if isinstance(slice_spec,
              (list, tuple)) and not isinstance(slice_spec, np.ndarray):
    is_index = True
    for s in slice_spec:
        if s is None or s is Ellipsis or isinstance(s, (list, tuple, slice)):
            is_index = False
            break
        elif isinstance(s, (np_arrays.ndarray, np.ndarray)) and s.ndim != 0:
            is_index = False
            break
    if not is_index:
        exit(tuple(slice_spec))
exit((slice_spec,))
