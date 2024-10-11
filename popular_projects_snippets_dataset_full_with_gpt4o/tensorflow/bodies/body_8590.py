# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x = array_ops.ones([3, 3, 3, 3, 3, 3])

with self.device:
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"TensorHandle\((.|\n){1,150}\[...\], shape="):
        array_ops.identity(x)
