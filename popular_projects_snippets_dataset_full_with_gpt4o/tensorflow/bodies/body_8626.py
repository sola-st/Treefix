# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x = self.device.pack(
    [constant_op.constant([1., 2.]),
     constant_op.constant([5.])])
with self.device:
    y = x * 2.
self.assertEqual([None], y.shape.as_list())
self.assertAllClose([[2., 4.], [10.]], self.device.unpack(y))

different_axes = self.device.pack(
    [constant_op.constant([1., 2.]),
     constant_op.constant([[5.]])])
with self.assertRaisesRegex(Exception,
                            "components do not all have the same rank"):
    different_axes.shape  # pylint: disable=pointless-statement
