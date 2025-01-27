# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
sess = session.InteractiveSession()

# Build a graph that has a bad op in it (no kernel).
#
# This test currently does not link in any GPU kernels,
# which is why placing this is invalid.  If at some point
# GPU kernels are added to this test, some other different
# op / device combo should be chosen.
with ops.device('/device:GPU:0'):
    a = constant_op.constant(1.0, shape=[1, 2])

b = constant_op.constant(1.0, shape=[1, 2])

# Only run the valid op, this should work.
self.evaluate(b)

with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(a)
sess.close()
