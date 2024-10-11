# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
strings = ["pigs on the wing", "animals"]

with self.cached_session():
    tokens = string_ops.string_split(strings)
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(indices, [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0]])
    self.assertAllEqual(values, [b"pigs", b"on", b"the", b"wing", b"animals"])
    self.assertAllEqual(shape, [2, 4])
