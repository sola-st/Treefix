# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
ref = np.zeros(shape, dtype=updates.dtype)
exit(_NumpyScatterNd(ref, indices, updates, lambda p, u: u))
