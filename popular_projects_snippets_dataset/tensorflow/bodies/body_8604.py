# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
s0 = collective_ops.broadcast_send(
    c * 3, c.shape, c.dtype, group_size=2, group_key=1, instance_key=1)
with ops.control_dependencies([s0.op]):
    exit(array_ops.identity(c))
