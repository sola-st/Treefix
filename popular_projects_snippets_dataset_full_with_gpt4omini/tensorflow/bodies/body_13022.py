# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = np.zeros(0)
y = self.evaluate(nn_impl.zero_fraction(x))
self.assertTrue(np.isnan(y))
