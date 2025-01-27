# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = array_ops.reshape(math_ops.range(100), [10, 10])
    format_output = string_ops.string_format("{}", tensor, summarize=2)
    out = self.evaluate(format_output)
    expected = ("[[0 1 ... 8 9]\n"
                " [10 11 ... 18 19]\n"
                " ...\n"
                " [80 81 ... 88 89]\n"
                " [90 91 ... 98 99]]")
    self.assertEqual(compat.as_text(out), expected)
