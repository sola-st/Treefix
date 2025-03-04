# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = [-4, -3, -2, -1, 0, 1, 2, 3]
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Source format must be of length 4 or 5"):
    op = nn_ops.data_format_dim_map(
        x, src_format="12345678", dst_format="87654321")
    with test_util.use_gpu():
        self.evaluate(op)
