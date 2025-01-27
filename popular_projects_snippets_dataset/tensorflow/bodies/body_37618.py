# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor, summarize=1)
    self.evaluate(print_op)

expected = "[0 ... 9]"
self.assertIn((expected + "\n"), printed.contents())

tensor = math_ops.range(10)
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor, summarize=2)
    self.evaluate(print_op)

expected = "[0 1 ... 8 9]"
self.assertIn((expected + "\n"), printed.contents())

tensor = math_ops.range(10)
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor, summarize=3)
    self.evaluate(print_op)

expected = "[0 1 2 ... 7 8 9]"
self.assertIn((expected + "\n"), printed.contents())

tensor = math_ops.range(10)
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor, summarize=-1)
    self.evaluate(print_op)

expected = "[0 1 2 3 4 5 6 7 8 9]"
self.assertIn((expected + "\n"), printed.contents())
