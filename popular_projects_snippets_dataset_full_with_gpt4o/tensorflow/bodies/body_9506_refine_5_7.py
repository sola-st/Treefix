import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertEqual': lambda self, a, b: a == b})() # pragma: no cover

import unittest # pragma: no cover

sess = type('MockSess', (object,), { 'partial_run_setup': lambda self, fetches, feeds: 1, 'partial_run': lambda self, handle, target, feed_dict: (feed_dict.get(a, 1) + feed_dict.get(b, 2)) * feed_dict.get(c, 1) })() # pragma: no cover
self = type('MockSelf', (unittest.TestCase,), {'assertEqual': lambda self, a, b: unittest.TestCase.assertEqual(self, a, b)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
from l3.Runtime import _l_
a = array_ops.placeholder(dtypes.float32, shape=[])
_l_(20014)
b = array_ops.placeholder(dtypes.float32, shape=[])
_l_(20015)
c = array_ops.placeholder(dtypes.float32, shape=[])
_l_(20016)
r1 = math_ops.add(a, b)
_l_(20017)
r2 = math_ops.multiply(r1, c)
_l_(20018)

h = sess.partial_run_setup([r1, r2], [a, b, c])
_l_(20019)
res = sess.partial_run(h, r1, feed_dict={a: 1, b: 2})
_l_(20020)
self.assertEqual(3, res)
_l_(20021)
temp = res * 17
_l_(20022)
res = sess.partial_run(h, r2, feed_dict={c: temp})
_l_(20023)
self.assertEqual(153, res)
_l_(20024)

# Call again on the same graph.
h2 = sess.partial_run_setup([r1, r2], [a, b, c])
_l_(20025)
res = sess.partial_run(h2, r1, feed_dict={a: 1, b: 2})
_l_(20026)
self.assertEqual(3, res)
_l_(20027)
temp = res * 18
_l_(20028)
res = sess.partial_run(h2, r2, feed_dict={c: temp})
_l_(20029)
self.assertEqual(162, res)
_l_(20030)
