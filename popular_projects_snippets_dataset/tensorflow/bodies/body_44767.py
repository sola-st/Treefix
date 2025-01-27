# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/misc_test.py
a = constant(1)
v = Variable(2)
s = 'a'
l = [1, 2, 3]

new_a, new_v, new_s, new_l = misc.alias_tensors(a, v, s, l)

self.assertFalse(new_a is a)
self.assertTrue(new_v is v)
self.assertTrue(new_s is s)
self.assertTrue(new_l is l)
with self.cached_session() as sess:
    self.assertEqual(1, self.evaluate(new_a))
