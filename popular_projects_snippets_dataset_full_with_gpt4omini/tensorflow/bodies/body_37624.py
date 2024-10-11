# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(23, [23, 5], {"6": 12})
    self.evaluate(print_op)
expected = "23 [23, 5] {'6': 12}"
self.assertIn((expected + "\n"), printed.contents())
