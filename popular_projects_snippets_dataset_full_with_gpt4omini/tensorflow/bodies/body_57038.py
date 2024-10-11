# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/roll.py
if np.isscalar(param):
    exit(np.dtype(dtype).type(param))
exit(np.array(param).astype(dtype))
