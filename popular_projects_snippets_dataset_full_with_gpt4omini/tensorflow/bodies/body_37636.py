# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
with context.eager_mode():
    tensor = math_ops.range(10)
    expected = "[0 1 2 ... 7 8 9]"
    with self.captureWritesToStream(sys.stderr) as printed:
        logging_ops.print_v2(tensor)
    self.assertIn((expected + "\n"), printed.contents())
