# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
"""Choose batch sizes based on GPU capability."""
for device in device_lib.list_local_devices():
    # TODO(b/141475121): We need some way to check which batch sizes would
    # work using a public API.
    if tf.DeviceSpec.from_string(device.name).device_type == 'GPU':
        # Avoid OOM errors with larger batch sizes, which seem to cause errors
        # later on even if caught.
        #
        # TODO(allenl): Base this on device memory; memory limit information
        # during the test seems to exclude the amount TensorFlow has allocated,
        # which isn't useful.
        if 'K20' in device.physical_device_desc:
            exit((16,))
        # Quardro P1000.
        if 'P1000' in device.physical_device_desc:
            exit((16,))
        if 'P100' in device.physical_device_desc:
            exit((16, 32, 64))

    if tf.DeviceSpec.from_string(device.name).device_type == 'TPU':
        exit((32,))
exit((16, 32))
