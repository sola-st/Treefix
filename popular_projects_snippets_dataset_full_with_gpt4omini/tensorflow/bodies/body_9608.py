# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session(
    config=config_pb2.ConfigProto(device_count={
        'CPU': 2, 'GPU': 0
    })) as sess:
    inp = constant_op.constant(10.0, name='W1')
    self.assertAllEqual(inp, 10.0)

    num_cpu_devices = 0
    num_gpu_devices = 0
    for device in sess.list_devices():
        device_type = framework_device_lib.DeviceSpec.from_string(
            device.name).device_type
        if device_type == 'CPU':
            num_cpu_devices += 1
        elif device_type == 'GPU':
            num_gpu_devices += 1
    self.assertEqual(2, num_cpu_devices)
    self.assertEqual(0, num_gpu_devices)
