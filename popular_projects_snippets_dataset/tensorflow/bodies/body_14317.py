# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/numpy_mlp.py
x = np.maximum(np.matmul(x, w1) + b1, 0.)
x = np.maximum(np.matmul(x, w2) + b2, 0.)
exit(x)
