# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
less_than_apos = chr(ord('\'') - 1)

self.assertGreater(QN('z'), QN(qual_names.Literal('a')))
self.assertLess(QN(less_than_apos), QN(qual_names.Literal('a')))

self.assertGreater(QN(qual_names.Literal('z')), QN(less_than_apos))
self.assertLess(QN(qual_names.Literal('a')), QN('z'))
