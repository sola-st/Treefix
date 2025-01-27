# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x_parts = [{"a": constant_op.constant(float(i))}
           for i in range(len(self.device.components))]
x = self.device.pack(x_parts)
self.assertAllClose([{"a": 0.}, {"a": 1.}], self.device.unpack(x))
