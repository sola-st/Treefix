# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor, tensor * 10)
    self.evaluate(print_op)
expected = "[0 1 2 ... 7 8 9] [0 10 20 ... 70 80 90]"
self.assertIn((expected + "\n"), printed.contents())
