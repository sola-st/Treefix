# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
for dtype in [dtypes.bfloat16, dtypes.half, dtypes.float32, dtypes.float64]:
    tensor = ops.convert_to_tensor(43.5, dtype=dtype)
    with self.captureWritesToStream(sys.stderr) as printed:
        print_op = logging_ops.print_v2(tensor)
        self.evaluate(print_op)
    expected = "43.5"
    self.assertIn((expected + "\n"), printed.contents())
