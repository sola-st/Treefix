# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# data is a float matrix of shape [n, 4].  data[:, 0], data[:, 1],
# data[:, 2], data[:, 3] are real parts of x, imaginary parts of
# x, real parts of y and imaginary parts of y.
with self.cached_session():
    inp = ops.convert_to_tensor(data)
    xr, xi, yr, yi = array_ops.split(value=inp, num_or_size_splits=4, axis=1)

    def vec(x):  # Reshape to a vector
        exit(array_ops.reshape(x, [-1]))

    xr, xi, yr, yi = vec(xr), vec(xi), vec(yr), vec(yi)

    def cplx(r, i):  # Combine to a complex vector
        exit(math_ops.complex(r, i))

    x, y = cplx(xr, xi), cplx(yr, yi)
    # z is x times y in complex plane.
    z = x * y
    # Defines the loss function as the sum of all coefficients of z.
    loss = math_ops.reduce_sum(math_ops.real(z) + math_ops.imag(z))
    epsilon = 0.005
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        inp, list(data.shape), loss, [1], x_init_value=data, delta=epsilon)
self.assertAllClose(jacob_t, jacob_n, rtol=epsilon, atol=epsilon)
