# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
a = QN('a')
a2 = QN('a')
a_b = QN(a, attr='b')
self.assertEqual(a2.qn, ('a',))
with self.assertRaises(ValueError):
    _ = a.parent

a_b2 = QN(a, attr='b')
self.assertEqual(a_b2.qn, (a, 'b'))
self.assertEqual(a_b2.parent.qn, ('a',))

self.assertTrue(a2 == a)
self.assertFalse(a2 is a)

self.assertTrue(a_b.parent == a)
self.assertTrue(a_b2.parent == a)

self.assertTrue(a_b2 == a_b)
self.assertFalse(a_b2 is a_b)
self.assertFalse(a_b2 == a)
a_sub_b = QN(a, subscript='b')
a_sub_b2 = QN(a, subscript='b')
self.assertTrue(a_sub_b == a_sub_b2)
self.assertFalse(a_sub_b == a_b)
