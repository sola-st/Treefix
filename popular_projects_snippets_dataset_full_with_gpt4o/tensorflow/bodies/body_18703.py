# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.TruncatedNormal(0.0, 1.0)
with self.assertRaises(ValueError):
    init([1], dtype=dtypes.int32)
