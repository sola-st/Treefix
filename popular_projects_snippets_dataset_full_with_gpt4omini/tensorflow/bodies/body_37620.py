# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
var_one = variables.Variable(2.14)
plus_one = var_one.assign_add(1.0)
var_two = variables.Variable(math_ops.range(10))
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())
with self.captureWritesToStream(sys.stderr) as printed:
    self.evaluate(plus_one)
    print_op = logging_ops.print_v2(var_one, {"second": var_two})
    self.evaluate(print_op)
expected = "3.14 {'second': [0 1 2 ... 7 8 9]}"
self.assertIn((expected + "\n"), printed.contents())
