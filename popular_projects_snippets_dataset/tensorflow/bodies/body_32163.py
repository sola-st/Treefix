# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
strings = ["", " a", "b ", " c", " ", " d ", ". e", "f .", " .g. ", " ."]

with self.cached_session():
    tokens = string_ops.string_split(strings, delimiter=" .")
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(
        indices,
        [[1, 0], [2, 0], [3, 0], [5, 0], [6, 0], [7, 0], [8, 0]])
    self.assertAllEqual(values, [b"a", b"b", b"c", b"d", b"e", b"f", b"g"])
    self.assertAllEqual(shape, [10, 1])
