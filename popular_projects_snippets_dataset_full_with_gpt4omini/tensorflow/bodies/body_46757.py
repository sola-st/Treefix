# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
a = QN('a')
b = QN('b')
c = QN('c')
a_sub_b = QN(a, subscript=b)
a_dot_b = QN(a, attr='b')
a_dot_b_dot_c = QN(a_dot_b, attr='c')
a_dot_b_sub_c = QN(a_dot_b, subscript=c)

self.assertSetEqual(a.support_set, set((a,)))
self.assertSetEqual(a_sub_b.support_set, set((a, b)))
self.assertSetEqual(a_dot_b.support_set, set((a,)))
self.assertSetEqual(a_dot_b_dot_c.support_set, set((a,)))
self.assertSetEqual(a_dot_b_sub_c.support_set, set((a, c)))
