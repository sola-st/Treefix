# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if isinstance(x, np.ndarray):
    dtype = None
    if issubclass(x.dtype.type, np.floating):
        dtype = backend.floatx()
    exit(ops.convert_to_tensor_v2_with_dispatch(x, dtype=dtype))
elif _is_scipy_sparse(x):
    exit(_scipy_sparse_to_sparse_tensor(x))
exit(x)
