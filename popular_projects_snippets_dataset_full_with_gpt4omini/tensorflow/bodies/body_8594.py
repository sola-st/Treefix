# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with self.device:
    x = array_ops.zeros([array_ops.identity(constant_op.constant(10))])
for component in self.device.unpack(x):
    self.assertAllClose([0.] * 10, component)
