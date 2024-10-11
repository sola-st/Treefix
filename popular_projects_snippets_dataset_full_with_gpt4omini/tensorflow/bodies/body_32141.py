# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = array_ops.reshape(math_ops.range(100), [10, 10])
    format_output = string_ops.string_format("tensor summary: {}", tensor,
                                             summarize=1)
    out = self.evaluate(format_output)
    expected = ("tensor summary: [[0 ... 9]\n"
                " ...\n"
                " [90 ... 99]]")
    self.assertEqual(compat.as_text(out), expected)
