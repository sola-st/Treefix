# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
a = QN('a')
self.assertEqual(a.qn, ('a',))
self.assertEqual(str(a), 'a')
self.assertEqual(a.ssf(), 'a')
self.assertEqual(a.ast().id, 'a')
self.assertFalse(a.is_composite())
with self.assertRaises(ValueError):
    _ = a.parent

a_b = QN(a, attr='b')
self.assertEqual(a_b.qn, (a, 'b'))
self.assertEqual(str(a_b), 'a.b')
self.assertEqual(a_b.ssf(), 'a_b')
self.assertEqual(a_b.ast().value.id, 'a')
self.assertEqual(a_b.ast().attr, 'b')
self.assertTrue(a_b.is_composite())
self.assertEqual(a_b.parent.qn, ('a',))
