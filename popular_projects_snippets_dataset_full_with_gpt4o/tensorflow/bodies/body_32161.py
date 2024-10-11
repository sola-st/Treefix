# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
strings = ["hello", "hola", b"\xF0\x9F\x98\x8E"]  # Last string is U+1F60E

with self.cached_session():
    tokens = string_ops.string_split(strings, delimiter="")
    indices, values, shape = self.evaluate(tokens)
    self.assertAllEqual(indices, [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                                  [1, 0], [1, 1], [1, 2], [1, 3], [2, 0],
                                  [2, 1], [2, 2], [2, 3]])
    expected = np.array(
        [
            "h", "e", "l", "l", "o", "h", "o", "l", "a", b"\xf0", b"\x9f",
            b"\x98", b"\x8e"
        ],
        dtype="|S1")
    self.assertAllEqual(values.tolist(), expected)
    self.assertAllEqual(shape, [3, 5])
