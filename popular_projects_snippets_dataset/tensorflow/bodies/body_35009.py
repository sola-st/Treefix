# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
student = student_t.StudentT(df=[7., 11.], loc=[[5.], [6.]], scale=3.)
self.assertAllEqual([], student.event_shape)
self.assertAllEqual([], self.evaluate(student.event_shape_tensor()))
self.assertAllEqual([2, 2], student.batch_shape)
self.assertAllEqual([2, 2], self.evaluate(student.batch_shape_tensor()))
num = 50000
samples = student.sample(num, seed=123456)
pdfs = student.prob(samples)
sample_vals, pdf_vals = self.evaluate([samples, pdfs])
self.assertEqual(samples.get_shape(), (num, 2, 2))
self.assertEqual(pdfs.get_shape(), (num, 2, 2))
self.assertNear(5., np.mean(sample_vals[:, 0, :]), err=0.1)
self.assertNear(6., np.mean(sample_vals[:, 1, :]), err=0.1)
self._assertIntegral(sample_vals[:, 0, 0], pdf_vals[:, 0, 0], err=0.05)
self._assertIntegral(sample_vals[:, 0, 1], pdf_vals[:, 0, 1], err=0.05)
self._assertIntegral(sample_vals[:, 1, 0], pdf_vals[:, 1, 0], err=0.05)
self._assertIntegral(sample_vals[:, 1, 1], pdf_vals[:, 1, 1], err=0.05)
if not stats:
    exit()
self.assertNear(
    stats.t.var(7., loc=0., scale=3.),  # loc d.n. effect var
    np.var(sample_vals[:, :, 0]),
    err=1.0)
self.assertNear(
    stats.t.var(11., loc=0., scale=3.),  # loc d.n. effect var
    np.var(sample_vals[:, :, 1]),
    err=1.0)
