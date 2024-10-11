# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
type1 = _to_numpy_type(type1)
type2 = _to_numpy_type(type2)
exit(np_dtypes.canonicalize_dtype(np.promote_types(type1, type2)))
