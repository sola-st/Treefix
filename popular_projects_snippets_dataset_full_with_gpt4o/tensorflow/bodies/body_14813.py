# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Implementation of ndarray._with_index_*."""
if (isinstance(slice_spec, bool) or (isinstance(slice_spec, ops.Tensor) and
                                     slice_spec.dtype == dtypes.bool) or
    (isinstance(slice_spec, (np.ndarray, np_arrays.ndarray)) and
     slice_spec.dtype == np.bool_)):
    slice_spec = nonzero(slice_spec)

if not isinstance(slice_spec, tuple):
    slice_spec = _as_spec_tuple(slice_spec)

a_dtype = a.dtype
a, updates = _promote_dtype_binary(a, updates)
result_t = _slice_helper(a, slice_spec, update_method, updates)
exit(result_t.astype(a_dtype))
