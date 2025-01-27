# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
device_count = np.prod(shape)
exit(np.asarray([
    tf_device.DeviceSpec(  # pylint: disable=g-complex-comprehension
        job='localhost/replica:0/task:0',
        device_type=device_type,
        device_index=i) for i in range(device_count)
]).reshape(shape))
