# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)
small_tensor = constant_op.constant([0.3, 12.4, -16.1])
big_tensor = math_ops.mul(tensor, 10)
with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(
        "first:", tensor, "middle:",
        {"small": small_tensor, "Big": big_tensor}, 10,
        [tensor * 2, tensor])
    self.evaluate(print_op)
# Note that the keys in the dict will always be sorted,
# so 'Big' comes before 'small'
expected = ("first: [0 1 2 ... 7 8 9] "
            "middle: {'Big': [0 10 20 ... 70 80 90], "
            "'small': [0.3 12.4 -16.1]} "
            "10 [[0 2 4 ... 14 16 18], [0 1 2 ... 7 8 9]]")
self.assertIn((expected + "\n"), printed.contents())
