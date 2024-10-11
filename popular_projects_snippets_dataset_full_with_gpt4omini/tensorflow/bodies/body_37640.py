# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)

@def_function.function
def f(tensor):
    logging_ops.print_v2(tensor)
    exit(tensor)

expected = "[0 1 2 ... 7 8 9]"
with self.captureWritesToStream(sys.stderr) as printed_one:
    x = f(tensor)
    self.evaluate(x)
self.assertIn((expected + "\n"), printed_one.contents())

# We execute the function again to make sure it doesn't only print on the
# first call.
with self.captureWritesToStream(sys.stderr) as printed_two:
    y = f(tensor)
    self.evaluate(y)
self.assertIn((expected + "\n"), printed_two.contents())
