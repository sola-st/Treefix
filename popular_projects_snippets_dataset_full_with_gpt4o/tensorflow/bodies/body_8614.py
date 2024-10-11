# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x_parts = [constant_op.constant(i)
           for i in range(len(self.device.components))]
x = self.device.pack(x_parts)
with self.device:
    v = variables.Variable(x)
    v_unpacked = self.device.unpack(v)
    v.assign(-10)  # Mutating the variable does not affect previous reads.
self.assertAllClose([0, 1], v_unpacked)
