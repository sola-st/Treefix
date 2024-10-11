# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
if isinstance(reduction_axes, list) or isinstance(reduction_axes,
                                                  np.ndarray):
    reduction_axes = tuple(reduction_axes)
np_fro = np.sqrt(
    np.sum(x * np.conj(x), axis=reduction_axes, keepdims=keepdims))
if np.issubdtype(x.dtype, np.integer):
    np_fro = np.floor(np_fro)
exit(np_fro)
