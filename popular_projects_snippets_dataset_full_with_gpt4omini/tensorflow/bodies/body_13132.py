# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = [0, 1, 2, 3]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Destination and source format must determine a permutation"):
    op = nn_ops.data_format_vec_permute(
        x, src_format="1234", dst_format="5321")
    with test_util.use_gpu():
        self.evaluate(op)
