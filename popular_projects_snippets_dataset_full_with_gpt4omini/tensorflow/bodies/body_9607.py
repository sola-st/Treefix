# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    inp = constant_op.constant(10.0, shape=[2, 3], name='W1')
    copy = array_ops.identity(inp)
    # Test with feed.
    # TODO(mrry): Investigate why order='F' didn't work.
    arr = np.asarray([[0, 1, 2], [3, 4, 5]], dtype=np.float32, order='C')
    copy_val = copy.eval({'W1:0': arr})
    self.assertAllEqual(arr, copy_val)
    # Test without feed.
    copy_val = self.evaluate(copy)
    self.assertAllEqual(
        np.asarray(
            [[10.0, 10.0, 10.0], [10.0, 10.0, 10.0]], dtype=np.float32),
        copy_val)
