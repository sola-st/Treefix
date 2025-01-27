# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x = self.device.pack(
    [constant_op.constant([5., 6.]),
     constant_op.constant([6., 7.])])
with self.device:
    x = transform(x)
parallel_str = str(x)
self.assertIn("5", parallel_str)
self.assertIn("7", parallel_str)
self.assertIn(self.device_type + ":0", parallel_str)
self.assertIn(self.device_type + ":1", parallel_str)
parallel_repr = repr(x)
self.assertIn("5", parallel_repr)
self.assertIn("7", parallel_repr)
self.assertIn(self.device_type + ":0", parallel_repr)
self.assertIn(self.device_type + ":1", parallel_repr)
