# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
x = _maybe_complex(np.random.rand(10, 10).astype(value_dtype))
x[np.abs(x) < 0.5] = 0  # Make it sparse

y = _maybe_complex(np.random.randn(10, 20).astype(value_dtype))

self._testMatmul(x, y, indices_dtype=indices_dtype)
