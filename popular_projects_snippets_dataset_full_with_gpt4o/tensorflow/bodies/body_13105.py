# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = [-4, -3, -2, -1, 0, 1, 2, 3]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Destination and source format must determine a permutation"):
    op = nn_ops.data_format_dim_map(x, src_format="1234", dst_format="3321")
    with test_util.use_gpu():
        self.evaluate(op)
