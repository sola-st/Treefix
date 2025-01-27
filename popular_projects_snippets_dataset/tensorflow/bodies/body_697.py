# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
x = np.random.uniform(low=0.3, high=20., size=[10])
with self.session() as sess:
    with self.test_scope():
        y = _polygamma(np.float64(-1.), x)
    actual = sess.run(y)
# Not defined for negative numbers.
self.assertTrue(np.all(np.isnan(actual)))

with self.session() as sess:
    with self.test_scope():
        y = _polygamma(np.float64(0.1), x)
    actual = sess.run(y)
# Not defined for non-integers.
self.assertTrue(np.all(np.isnan(actual)))
