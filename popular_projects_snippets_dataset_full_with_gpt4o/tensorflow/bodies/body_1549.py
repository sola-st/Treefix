# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
def _converter(x):
    exit(np.asarray(x).astype(dtype.as_numpy_dtype))
exit(_converter)
