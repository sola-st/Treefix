# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/misc_test.py
a = constant(1)

new_a = misc.alias_tensors(a)
self.assertFalse(new_a is a)
with self.cached_session() as sess:
    self.assertEqual(1, self.evaluate(new_a))
