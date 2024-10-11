# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
a = QN('a')
a_sub_str_b = QN(a, subscript=QN(qual_names.Literal('b')))
a_sub_b = QN(a, subscript=QN('b'))

self.assertNotEqual(a_sub_str_b, a_sub_b)
self.assertNotEqual(hash(a_sub_str_b), hash(a_sub_b))
self.assertEqual(a_sub_str_b.ast().slice.value, 'b')
self.assertEqual(str(a_sub_str_b), "a['b']")

a_sub_three = QN(a, subscript=QN(qual_names.Literal(3)))
self.assertEqual(a_sub_three.ast().slice.value, 3)
self.assertEqual(str(a_sub_three), 'a[3]')
