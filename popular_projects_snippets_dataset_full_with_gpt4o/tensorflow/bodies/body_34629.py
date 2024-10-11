# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [
    constant_op.constant([2]),
    constant_op.constant([1]),
    constant_op.constant([0]),
    constant_op.constant([3]),
]
data = [
    constant_op.constant([1.0]),
    constant_op.constant([2.0]),
    constant_op.constant([3.0]),
    constant_op.constant([4.0])
]
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "expected inputs .* do not match|List argument .* must match"):
    self.evaluate(data_flow_ops.dynamic_stitch(indices[0:2], data))

with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "expected inputs .* do not match|List argument .* must match"):
    self.evaluate(data_flow_ops.dynamic_stitch(indices, data[0:2]))
