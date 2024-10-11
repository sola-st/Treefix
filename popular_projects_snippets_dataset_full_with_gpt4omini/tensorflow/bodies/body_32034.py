# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_length_op_test.py
# Code that predates the 'unit' parameter may have used a positional
# argument for the 'name' parameter.  Check that we don't break such code.
strings = [[["1", "12"], ["123", "1234"], ["12345", "123456"]]]
lengths = string_ops.string_length(strings, "some_name")
with self.session():
    self.assertAllEqual(lengths, [[[1, 2], [3, 4], [5, 6]]])
