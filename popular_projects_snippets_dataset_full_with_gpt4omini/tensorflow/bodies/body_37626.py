# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = ops.convert_to_tensor("scalar")
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor)
    self.evaluate(print_op)
expected = "scalar"
self.assertIn((expected + "\n"), printed.contents())
