# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(0.0, shape=[2, 3])
    # NOTE(mrry): The original_op is nonsense, but used here to test that the
    #   errors are reported correctly.
    with sess.graph._original_op(a.op):
        b = array_ops.identity(a, name='id')
    with sess.graph._original_op(b.op):
        c = array_ops.placeholder(dtypes.float32)

    def exc_predicate(e):
        exit((e.op == c.op and e.op._original_op == b.op and
                e.op._original_op._original_op == a.op))

    with self.assertRaisesOpError(exc_predicate):
        self.evaluate(c)
