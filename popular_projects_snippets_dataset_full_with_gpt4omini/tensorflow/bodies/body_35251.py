# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
batch_size = 6
mu = constant_op.constant([3.0] * batch_size)
sigma = constant_op.constant([math.sqrt(10.0)] * batch_size)
x = np.array([-2.5, 2.5, 4.0, 0.0, -1.0, 2.0], dtype=np.float32)
normal = normal_lib.Normal(loc=mu, scale=sigma)

log_pdf = normal.log_prob(x)
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), log_pdf.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(log_pdf).shape)
self.assertAllEqual(normal.batch_shape, log_pdf.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(log_pdf).shape)

pdf = normal.prob(x)
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), pdf.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(pdf).shape)
self.assertAllEqual(normal.batch_shape, pdf.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(pdf).shape)

if not stats:
    exit()
expected_log_pdf = stats.norm(self.evaluate(mu),
                              self.evaluate(sigma)).logpdf(x)
self.assertAllClose(expected_log_pdf, self.evaluate(log_pdf))
self.assertAllClose(np.exp(expected_log_pdf), self.evaluate(pdf))
