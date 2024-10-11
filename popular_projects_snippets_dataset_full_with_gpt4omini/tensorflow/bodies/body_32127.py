# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    var_one = variables.Variable(2.14)
    plus_one = var_one.assign_add(1.0)
    var_two = variables.Variable(math_ops.range(10))
    format_output = string_ops.string_format("{}, {}", [var_one, var_two])
    if not context.executing_eagerly():
        self.evaluate(variables.global_variables_initializer())
    self.evaluate(plus_one)
    out = self.evaluate(format_output)
    expected = "3.14, [0 1 2 ... 7 8 9]"
    self.assertEqual(compat.as_text(out), expected)
