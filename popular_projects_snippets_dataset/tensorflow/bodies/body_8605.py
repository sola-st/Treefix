# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
r0 = collective_ops.broadcast_recv(
    c.shape, c.dtype, group_size=2, group_key=1, instance_key=1)
exit(r0)
