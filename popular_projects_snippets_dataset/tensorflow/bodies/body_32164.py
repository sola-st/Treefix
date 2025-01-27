# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
strings = ["hello|world", "hello world"]

with self.cached_session():
    self.assertRaises(
        ValueError, string_ops.string_split, strings, delimiter=["|", ""])

    self.assertRaises(
        ValueError, string_ops.string_split, strings, delimiter=["a"])

    tokens = string_ops.string_split(strings, delimiter="|")
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(indices, [[0, 0], [0, 1], [1, 0]])
    self.assertAllEqual(values, [b"hello", b"world", b"hello world"])
    self.assertAllEqual(shape, [2, 2])

    tokens = string_ops.string_split(strings, delimiter="| ")
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(indices, [[0, 0], [0, 1], [1, 0], [1, 1]])
    self.assertAllEqual(values, [b"hello", b"world", b"hello", b"world"])
    self.assertAllEqual(shape, [2, 2])
