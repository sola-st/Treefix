# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
a = QN('a')
b = QN('b')
c = QN('c')
b_sub_c = QN(b, subscript=c)
a_sub_b_sub_c = QN(a, subscript=b_sub_c)

b_dot_c = QN(b, attr='c')
a_sub__b_dot_c = QN(a, subscript=b_dot_c)

a_sub_b = QN(a, subscript=b)
a_sub_b__dot_c = QN(a_sub_b, attr='c')

a_dot_b = QN(a, attr='b')
a_dot_b_sub_c = QN(a_dot_b, subscript=c)

self.assertEqual(str(a_sub_b_sub_c), 'a[b[c]]')
self.assertEqual(str(a_sub__b_dot_c), 'a[b.c]')
self.assertEqual(str(a_sub_b__dot_c), 'a[b].c')
self.assertEqual(str(a_dot_b_sub_c), 'a.b[c]')

self.assertNotEqual(a_sub_b_sub_c, a_sub__b_dot_c)
self.assertNotEqual(a_sub_b_sub_c, a_sub_b__dot_c)
self.assertNotEqual(a_sub_b_sub_c, a_dot_b_sub_c)

self.assertNotEqual(a_sub__b_dot_c, a_sub_b__dot_c)
self.assertNotEqual(a_sub__b_dot_c, a_dot_b_sub_c)

self.assertNotEqual(a_sub_b__dot_c, a_dot_b_sub_c)
