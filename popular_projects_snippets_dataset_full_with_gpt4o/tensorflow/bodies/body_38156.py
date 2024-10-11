# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
with test_util.force_cpu():
    inx = ops.convert_to_tensor(x, dtype=dtype)
    z = func(inx, y)  # Should use __add__, __sub__, etc.
    exit(self.evaluate(z))
