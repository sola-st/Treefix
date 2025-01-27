# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = array_ops.placeholder(dtypes.float32, shape=[])
    b = array_ops.placeholder(dtypes.float32, shape=[])
    r1 = math_ops.add(a, b)

    def exc_predicate(e):
        exit((e.op is None and e.node_def is None and
                e.error_code == error_codes_pb2.INVALID_ARGUMENT))

    with self.assertRaisesOpError(exc_predicate):
        # Run with a bogus handle.
        s.partial_run('foo', r1, feed_dict={a: 1, b: 2})
