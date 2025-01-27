# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
gamma = gamma_lib.Gamma(concentration=[7., 11.], rate=[[5.], [6.]])
num = 50000
samples = gamma.sample(num, seed=137)
pdfs = gamma.prob(samples)
sample_vals, pdf_vals = self.evaluate([samples, pdfs])
self.assertEqual(samples.get_shape(), (num, 2, 2))
self.assertEqual(pdfs.get_shape(), (num, 2, 2))
self._assertIntegral(sample_vals[:, 0, 0], pdf_vals[:, 0, 0], err=0.02)
self._assertIntegral(sample_vals[:, 0, 1], pdf_vals[:, 0, 1], err=0.02)
self._assertIntegral(sample_vals[:, 1, 0], pdf_vals[:, 1, 0], err=0.02)
self._assertIntegral(sample_vals[:, 1, 1], pdf_vals[:, 1, 1], err=0.02)
if not stats:
    exit()
self.assertAllClose(
    stats.gamma.mean([[7., 11.], [7., 11.]],
                     scale=1 / np.array([[5., 5.], [6., 6.]])),
    sample_vals.mean(axis=0),
    atol=.1)
self.assertAllClose(
    stats.gamma.var([[7., 11.], [7., 11.]],
                    scale=1 / np.array([[5., 5.], [6., 6.]])),
    sample_vals.var(axis=0),
    atol=.1)
