class MockSession:# pragma: no cover
    def partial_run_setup(self, fetches, feeds):# pragma: no cover
        return 'handle'# pragma: no cover
    def partial_run(self, handle, fetch, feed_dict):# pragma: no cover
        if fetch == r1:# pragma: no cover
            return feed_dict[a] + feed_dict[b]# pragma: no cover
        elif fetch == r2:# pragma: no cover
            return (feed_dict[a] + feed_dict[b]) * feed_dict[c]# pragma: no cover
sess = MockSession() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertEqual(x, y):# pragma: no cover
        assert x == y, f'Assertion Failed: {x} != {y}'# pragma: no cover
self = MockSelf() # pragma: no cover

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
