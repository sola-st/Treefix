# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical_test.py
with self.cached_session() as sess:
    t = logical.or_(self._tf_false, self._tf_true)
    self.assertEqual(self.evaluate(t), True)
    t = logical.or_(self._tf_false, lambda: True)
    self.assertEqual(self.evaluate(t), True)
    t = logical.or_(self._tf_true, lambda: True)
    self.assertEqual(self.evaluate(t), True)
    # TODO(mdan): Add a test for ops with side effects.
