# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = [[0, 1], [2, 3]]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Format specifier must contain H and W for 2D case"):
    op = nn_ops.data_format_vec_permute(
        x, src_format="1234", dst_format="4321")
    with test_util.use_gpu():
        self.evaluate(op)
