# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
strings = ["#a", "b#", "#c#"]

with self.cached_session():
    tokens = string_ops.string_split(strings, "#", skip_empty=False)
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(indices, [[0, 0], [0, 1],
                                  [1, 0], [1, 1],
                                  [2, 0], [2, 1], [2, 2]])
    self.assertAllEqual(values, [b"", b"a", b"b", b"", b"", b"c", b""])
    self.assertAllEqual(shape, [3, 3])

with self.cached_session():
    tokens = string_ops.string_split(strings, "#")
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(values, [b"a", b"b", b"c"])
    self.assertAllEqual(indices, [[0, 0], [1, 0], [2, 0]])
    self.assertAllEqual(shape, [3, 1])
