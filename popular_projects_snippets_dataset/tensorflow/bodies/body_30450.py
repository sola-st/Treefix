# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
with self.cached_session():
    x = [[1, 2, 3], [4, 5, 6]]
    with self.assertRaisesRegex(
        ValueError,
        "Value of argument `mode` expected to be .* Received `mode` = WEIRD"):
        self.evaluate(array_ops.pad(x, [[1, 0], [2, 1]], mode="weird"))
