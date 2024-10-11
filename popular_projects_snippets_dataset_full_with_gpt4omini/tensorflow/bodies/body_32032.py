# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_length_op_test.py
strings = [[["1", "12"], ["123", "1234"], ["12345", "123456"]]]

with self.cached_session() as sess:
    lengths = string_ops.string_length(strings)
    values = self.evaluate(lengths)
    self.assertAllEqual(values, [[[1, 2], [3, 4], [5, 6]]])
