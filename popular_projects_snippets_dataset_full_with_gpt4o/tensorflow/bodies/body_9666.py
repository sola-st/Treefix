# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
sess = session.Session()

# Build a graph that has a bad op in it (no kernel).
#
# This test currently does not link in any GPU kernels,
# which is why placing this is invalid.  If at some point
# GPU kernels are added to this test, some other different
# op / device combo should be chosen.
with ops.device('/device:GPU:0'):
    _ = constant_op.constant(1.0, shape=[1, 2])

b = constant_op.constant(1.0, shape=[1, 2])

with self.assertRaises(errors.InvalidArgumentError):
    # Even though we don't run the bad op, we place the entire
    # graph, which should fail with a non-interactive session.
    sess.run(b)

sess.close()
