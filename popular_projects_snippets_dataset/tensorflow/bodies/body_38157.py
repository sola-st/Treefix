# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
with test_util.force_cpu():
    iny = ops.convert_to_tensor(y, dtype=dtype)
    z = func(x, iny)  # Should use __radd__, __rsub__, etc.
    exit(self.evaluate(z))
