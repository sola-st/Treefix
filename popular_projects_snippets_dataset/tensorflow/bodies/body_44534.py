# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/exceptions_test.py
with self.cached_session() as sess:
    t = exceptions.assert_stmt(
        constant_op.constant(True), lambda: constant_op.constant('ignored'))
    self.evaluate(t)
