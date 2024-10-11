self = type('Mock', (object,), {'assertEqual': lambda x, y: print(f'Assert: {x} == {y}')})() # pragma: no cover

self = type('Mock', (object,), {'assertEqual': lambda x, y: print(f'Assert: {x} == {y}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
from l3.Runtime import _l_
a = array_ops.placeholder(dtypes.float32, shape=[])
_l_(7116)
b = array_ops.placeholder(dtypes.float32, shape=[])
_l_(7117)
c = array_ops.placeholder(dtypes.float32, shape=[])
_l_(7118)
r1 = math_ops.add(a, b)
_l_(7119)
r2 = math_ops.multiply(r1, c)
_l_(7120)

h = sess.partial_run_setup([r1, r2], [a, b, c])
_l_(7121)
res = sess.partial_run(h, r1, feed_dict={a: 1, b: 2})
_l_(7122)
self.assertEqual(3, res)
_l_(7123)
temp = res * 17
_l_(7124)
res = sess.partial_run(h, r2, feed_dict={c: temp})
_l_(7125)
self.assertEqual(153, res)
_l_(7126)

# Call again on the same graph.
h2 = sess.partial_run_setup([r1, r2], [a, b, c])
_l_(7127)
res = sess.partial_run(h2, r1, feed_dict={a: 1, b: 2})
_l_(7128)
self.assertEqual(3, res)
_l_(7129)
temp = res * 18
_l_(7130)
res = sess.partial_run(h2, r2, feed_dict={c: temp})
_l_(7131)
self.assertEqual(162, res)
_l_(7132)
