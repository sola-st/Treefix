# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x_parts = [variables.Variable(i)
           for i in range(len(self.device.components))]
x = self.device.pack(x_parts)
with self.device:
    x1 = self.device.pack(x_parts)
for v in x_parts:
    v.assign(-10)  # Mutating the variable does not affect previous reads.
self.assertAllClose([0, 1], self.device.unpack(x))
self.assertAllClose([0, 1], self.device.unpack(x1))
