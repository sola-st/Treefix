# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
a = QN('a')
b = QN('b')
a_dot_b = QN(a, attr='b')
a_sub_b = QN(a, subscript=b)
self.assertEqual(qual_names.from_str('a.b'), a_dot_b)
self.assertEqual(qual_names.from_str('a'), a)
self.assertEqual(qual_names.from_str('a[b]'), a_sub_b)
