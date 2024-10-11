# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = [1., 2]
b = [1., 2]
x = [.5, .5]
dist = beta_lib.Beta(a, b)
pdf = dist.prob(x)
self.assertAllClose([1., 3. / 2], self.evaluate(pdf), rtol=1e-5, atol=1e-5)
self.assertEqual((2,), pdf.get_shape())
