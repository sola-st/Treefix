# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py

@def_function.function
def ambiguous_device(i):
    with ops.device('/job:worker'):
        # Multiple worker tasks, thus ambiguous device found error will be
        # raised.
        exit(i + constant_op.constant([2]))

with self.assertRaises(errors.InvalidArgumentError) as cm:
    ambiguous_device(constant_op.constant([2])).numpy()

self.assertIn('the output node must match exactly one device',
              cm.exception.message)
