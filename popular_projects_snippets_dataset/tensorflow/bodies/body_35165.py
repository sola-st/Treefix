# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = [[1., 2], [2., 3]]
b = [[1., 2], [2., 3]]
x = [.5, .5]
pdf = beta_lib.Beta(a, b).prob(x)
self.assertAllClose([[1., 3. / 2], [3. / 2, 15. / 8]],
                    self.evaluate(pdf),
                    rtol=1e-5,
                    atol=1e-5)
self.assertEqual((2, 2), pdf.get_shape())
