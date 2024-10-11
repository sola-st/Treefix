# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.Identity()
self.assertRaises(ValueError, init, shape=[10, 5], dtype=dtypes.int32)
