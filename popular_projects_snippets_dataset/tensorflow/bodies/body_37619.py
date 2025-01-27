# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
var = variables.Variable(math_ops.range(10))
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(var)
    self.evaluate(print_op)
expected = "[0 1 2 ... 7 8 9]"
self.assertIn((expected + "\n"), printed.contents())
