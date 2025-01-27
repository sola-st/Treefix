# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
student = student_t.StudentT(df=3., loc=np.pi, scale=1.)
num = 20000
samples = student.sample(num, seed=123456)
pdfs = student.prob(samples)
mean = student.mean()
mean_pdf = student.prob(student.mean())
sample_vals, pdf_vals, mean_val, mean_pdf_val = self.evaluate(
    [samples, pdfs, student.mean(), mean_pdf])
self.assertEqual(samples.get_shape(), (num,))
self.assertEqual(pdfs.get_shape(), (num,))
self.assertEqual(mean.get_shape(), ())
self.assertNear(np.pi, np.mean(sample_vals), err=0.1)
self.assertNear(np.pi, mean_val, err=1e-6)
# Verify integral over sample*pdf ~= 1.
# Tolerance increased since eager was getting a value of 1.002041.
self._assertIntegral(sample_vals, pdf_vals, err=5e-2)
if not stats:
    exit()
self.assertNear(stats.t.pdf(np.pi, 3., loc=np.pi), mean_pdf_val, err=1e-6)
