# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.Zeros()
with self.assertRaisesRegex(
    TypeError, r"Keyword argument should be one of .* Received: dtpye"):
    init((2, 2), dtpye=dtypes.float32)
