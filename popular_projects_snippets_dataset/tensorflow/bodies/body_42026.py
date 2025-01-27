# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
a = constant_op.constant(1)
b = constant_op.constant(2)
# Right now we don't support soft device place on remote worker.
with self.assertRaises(errors.InvalidArgumentError) as cm:
    with ops.device('/job:worker/replica:0/task:0/device:GPU:42'):
        c = a + b
        del c
    self.assertIn('unknown device', cm.exception.message)
