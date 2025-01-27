# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
d = {QN('a'): 'a', QN('b'): 'b'}
self.assertEqual(d[QN('a')], 'a')
self.assertEqual(d[QN('b')], 'b')
self.assertNotIn(QN('c'), d)
