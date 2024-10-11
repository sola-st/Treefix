# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
q = np.random.uniform(low=0.3, high=20., size=[10])
with self.session() as sess:
    with self.test_scope():
        y = _zeta(np.float64(1.), q)
    actual = sess.run(y)
# When x == 1, this is the Harmonic series.
self.assertTrue(np.all(np.isinf(actual)))

with self.session() as sess:
    with self.test_scope():
        y = _zeta(np.float64(0.1), q)
    actual = sess.run(y)
# When x < 1, this is undefined.
self.assertTrue(np.all(np.isnan(actual)))

with self.session() as sess:
    with self.test_scope():
        y = _zeta([1.1, 1.2, 2.1, 2.2, 3.1], [-2.0, -1.1, -1.0, -0.5, -0.1])
    actual = sess.run(y)
# For q <= 0, x must be an integer.
self.assertTrue(np.all(np.isnan(actual)))

with self.session() as sess:
    with self.test_scope():
        y = _zeta([2.0, 4.0, 6.0], [0.0, -1.0, -2.0])
    actual = sess.run(y)
# For integer q <= 0, zeta has poles with a defined limit of +inf where x is
# an even integer.
self.assertTrue(np.all(np.isinf(actual)))

with self.session() as sess:
    with self.test_scope():
        y = _zeta([3.0, 5.0, 7.0], [0.0, -1.0, -2.0])
    actual = sess.run(y)
# For non-positive integer q, zeta has poles with an undefined limit where x
# is an odd integer.
self.assertTrue(np.all(np.isnan(actual)))

with self.session() as sess:
    with self.test_scope():
        y = _zeta([1.1, 2.2, 3.3], [-1.1, -1.0, 0.0])
    actual = sess.run(y)
# For non-positive q, zeta is not defined if x is not an integer.
self.assertTrue(np.all(np.isnan(actual)))
