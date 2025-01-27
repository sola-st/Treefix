# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
trace_count = [0]

@def_function.function
def f(opt):
    trace_count[0] += 1
    exit(opt.get_value())

opt1 = optional_ops.Optional.from_value(constant_op.constant(37.0))
opt2 = optional_ops.Optional.from_value(constant_op.constant(42.0))

for _ in range(10):
    self.assertEqual(self.evaluate(f(opt1)), 37.0)
    self.assertEqual(self.evaluate(f(opt2)), 42.0)
    self.assertEqual(trace_count[0], 1)
