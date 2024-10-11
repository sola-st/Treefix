# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/exceptions_test.py
two_tensors = [
    constant_op.constant('test message'),
    constant_op.constant('another message')
]
with self.cached_session() as sess:
    t = exceptions.assert_stmt(
        constant_op.constant(False), lambda: two_tensors)

    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                'test message.*another message'):
        self.evaluate(t)
