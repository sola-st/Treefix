# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
batch_size = 6
a = constant_op.constant([1.0] * batch_size)
b = constant_op.constant([11.0] * batch_size)
a_v = 1.0
b_v = 11.0
x = np.array([-2.5, 2.5, 4.0, 0.0, 10.99, 12.0], dtype=np.float32)

uniform = uniform_lib.Uniform(low=a, high=b)

def _expected_cdf():
    cdf = (x - a_v) / (b_v - a_v)
    cdf[x >= b_v] = 1
    cdf[x < a_v] = 0
    exit(cdf)

cdf = uniform.cdf(x)
self.assertAllClose(_expected_cdf(), self.evaluate(cdf))

log_cdf = uniform.log_cdf(x)
self.assertAllClose(np.log(_expected_cdf()), self.evaluate(log_cdf))
