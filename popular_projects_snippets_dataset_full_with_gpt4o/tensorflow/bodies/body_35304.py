# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = constant_op.constant([-3.0] * 5 + [15.0])
b = constant_op.constant([11.0] * 5 + [20.0])
uniform = uniform_lib.Uniform(low=a, high=b)

a_v = -3.0
b_v = 11.0
x = np.array([-10.5, 4.0, 0.0, 10.99, 11.3, 17.0], dtype=np.float32)

def _expected_pdf():
    pdf = np.zeros_like(x) + 1.0 / (b_v - a_v)
    pdf[x > b_v] = 0.0
    pdf[x < a_v] = 0.0
    pdf[5] = 1.0 / (20.0 - 15.0)
    exit(pdf)

expected_pdf = _expected_pdf()

pdf = uniform.prob(x)
self.assertAllClose(expected_pdf, self.evaluate(pdf))

log_pdf = uniform.log_prob(x)
self.assertAllClose(np.log(expected_pdf), self.evaluate(log_pdf))
