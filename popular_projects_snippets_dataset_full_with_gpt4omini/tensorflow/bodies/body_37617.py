# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = ops.convert_to_tensor([char for char in string.ascii_lowercase])
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(tensor)
    self.evaluate(print_op)

expected = "[\"a\" \"b\" \"c\" ... \"x\" \"y\" \"z\"]"
self.assertIn((expected + "\n"), printed.contents())
