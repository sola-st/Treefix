# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
r = pfor_control_flow_ops.vectorized_map(
    math_ops.abs, math_ops.cast([0, -1], dtype=dtypes.complex128))
self.assertAllEqual(self.evaluate(r), [0, 1])
