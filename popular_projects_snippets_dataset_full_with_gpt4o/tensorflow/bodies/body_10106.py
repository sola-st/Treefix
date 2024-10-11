# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
"""Test that previously revealed a bug in buffer forwarding for AddN."""
partials = []
for _ in range(98):
    partials.append(math_ops.add_n([constant_op.constant(1)]))
partials.append(
    math_ops.add_n([constant_op.constant(1),
                    constant_op.constant(1)]))

res = math_ops.add_n(partials) + constant_op.constant(0)
with test_util.use_gpu():
    self.assertAllEqual(res, 100)
