# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.Orthogonal()
self.assertRaises(ValueError, init, shape=(10, 10), dtype=dtypes.string)
