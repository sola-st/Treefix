# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/exceptions_test.py
with self.cached_session() as sess:
    t = exceptions.assert_stmt(
        constant_op.constant(False),
        lambda: constant_op.constant('test message'))

    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                'test message'):
        self.evaluate(t)
