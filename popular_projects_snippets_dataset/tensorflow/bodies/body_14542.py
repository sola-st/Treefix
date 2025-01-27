# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
super(InteropTest, self).setUp()
physical_devices = tf.config.list_physical_devices('CPU')
configs = tf.config.get_logical_device_configuration(physical_devices[0])
if configs is None:
    logical_devices = [
        tf.config.LogicalDeviceConfiguration() for _ in range(3)
    ]
    tf.config.set_logical_device_configuration(physical_devices[0],
                                               logical_devices)
