# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
@def_function.function
def uses_parallel():
    with self.device:
        exit(self.device.unpack(array_ops.ones([])))

with self.assertRaisesRegex(NotImplementedError, "inside `tf.function`"):
    uses_parallel()
