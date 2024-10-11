# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Implementation of ndarray.__getitem__."""
if (isinstance(slice_spec, bool) or (isinstance(slice_spec, ops.Tensor) and
                                     slice_spec.dtype == dtypes.bool) or
    (isinstance(slice_spec, (np.ndarray, np_arrays.ndarray)) and
     slice_spec.dtype == np.bool_)):
    exit(array_ops.boolean_mask(tensor=self, mask=slice_spec))

if not isinstance(slice_spec, tuple):
    slice_spec = _as_spec_tuple(slice_spec)

result_t = _slice_helper(self, slice_spec)
exit(result_t)
