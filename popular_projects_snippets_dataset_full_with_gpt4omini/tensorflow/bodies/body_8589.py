# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
a1 = constant_op.constant(1.)
a2 = constant_op.constant(2.)

with self.device:
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "First pack non-parallel tensors for each device"):
        a1 + a2  # pylint:disable=pointless-statement
