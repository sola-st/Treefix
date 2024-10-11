# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
n, m = size
x = np.random.randn(n, m).astype(np_dtype)
exit(_sparsify(x) if sparse else x)
