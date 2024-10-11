# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical_test.py
with self.cached_session() as sess:
    t = logical.and_(self._tf_true, self._tf_true)
    self.assertEqual(self.evaluate(t), True)
    t = logical.and_(self._tf_true, lambda: True)
    self.assertEqual(self.evaluate(t), True)
    t = logical.and_(self._tf_false, lambda: True)
    self.assertEqual(self.evaluate(t), False)
    # TODO(mdan): Add a test for ops with side effects.
