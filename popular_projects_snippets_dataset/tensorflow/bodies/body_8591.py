# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
device = parallel_device.ParallelDevice(components=[
    "/job:localhost/device:{}:0".format(self.device_type),
])
x = constant_op.constant([2, 3, 4])
with device:
    x = device.pack([x])
    if math_ops.reduce_any(math_ops.equal(x, constant_op.constant(4))):
        y = constant_op.constant(1)
    else:
        y = constant_op.constant(2)
self.assertAllEqual([1], device.unpack(y))
