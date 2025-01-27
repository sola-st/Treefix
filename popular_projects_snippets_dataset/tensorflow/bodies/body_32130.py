# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = math_ops.range(6)
    format_output = string_ops.string_format("{}", tensor, summarize=-1)
    out = self.evaluate(format_output)
    expected = "[0 1 2 3 4 5]"
    self.assertEqual(compat.as_text(out), expected)

with self.cached_session():
    tensor = math_ops.range(6)
    format_output = string_ops.string_format("{}", tensor, summarize=1)
    out = self.evaluate(format_output)
    expected = "[0 ... 5]"
    self.assertEqual(compat.as_text(out), expected)

with self.cached_session():
    tensor = math_ops.range(6)
    format_output = string_ops.string_format("{}", tensor, summarize=2)
    out = self.evaluate(format_output)
    expected = "[0 1 ... 4 5]"
    self.assertEqual(compat.as_text(out), expected)

with self.cached_session():
    tensor = math_ops.range(6)
    format_output = string_ops.string_format("{}", tensor, summarize=10)
    out = self.evaluate(format_output)
    expected = "[0 1 2 3 4 5]"
    self.assertEqual(compat.as_text(out), expected)
