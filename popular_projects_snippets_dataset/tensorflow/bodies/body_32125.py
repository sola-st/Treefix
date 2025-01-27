# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    var = variables.Variable(3.34)
    format_output = string_ops.string_format("{}", [var])
    if not context.executing_eagerly():
        self.evaluate(variables.global_variables_initializer())
    out = self.evaluate(format_output)
    expected = "3.34"
    self.assertEqual(compat.as_text(out), expected)
