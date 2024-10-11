# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = array_ops.reshape(math_ops.range(4), [2, 2])
    format_output = string_ops.string_format("{}", tensor, summarize=3)
    out = self.evaluate(format_output)
    expected = ("[[0 1]\n"
                " [2 3]]")
    self.assertEqual(compat.as_text(out), expected)
