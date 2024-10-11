# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with self.device:
    layer = _Dense(5)
    x = constant_op.constant([[2.]])
    y = layer(x)
    outputs = self.device.unpack(y)
self.assertAllClose([[3.] * 5], outputs[0])
self.assertAllClose([[3.] * 5], outputs[1])
self.assertIn(self.device.components[0], outputs[0].backing_device)
self.assertIn(self.device.components[1], outputs[1].backing_device)

# With different Layer inputs we get different outputs
x = self.device.pack(
    [constant_op.constant([[-0.5]]),
     constant_op.constant([[0.5]])])
with self.device:
    y = layer(x)
    outputs = self.device.unpack(y)
self.assertGreater(
    math_ops.reduce_max(math_ops.abs(outputs[0] - outputs[1])), 1e-5)
self.assertIn(self.device.components[0], outputs[0].backing_device)
self.assertIn(self.device.components[1], outputs[1].backing_device)
