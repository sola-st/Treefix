# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical_test.py
with self.cached_session() as sess:
    t = logical.not_(self._tf_false())
    self.assertEqual(self.evaluate(t), True)
