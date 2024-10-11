# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
x = np.random.rand(1000000) > 0.5
truth = np.vstack([np.where(x)[0].astype(np.int64)]).T
self._testWhere(x, truth, None, fn)
