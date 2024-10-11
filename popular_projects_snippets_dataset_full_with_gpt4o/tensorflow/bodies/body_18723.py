# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.Identity()
with self.assertRaisesWithLiteralMatch(
    ValueError,
    r"Identity initializer doesn't support partition-related arguments"):
    init((4, 2), dtype=dtypes.float32, partition_shape=(2, 2))
