# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# x[:, 0] is real, x[:, 1] is imag.  We combine real and imag into
# complex numbers. Then, we extract real and imag parts and
# computes the squared sum. This is obviously the same as sum(real
# * real) + sum(imag * imag). We just want to make sure the
# gradient function is checked.
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    real, imag = array_ops.split(value=inx, num_or_size_splits=2, axis=1)
    real, imag = array_ops.reshape(real, [-1]), array_ops.reshape(imag, [-1])
    cplx = math_ops.complex(real, imag)
    cplx = math_ops.conj(cplx)
    loss = math_ops.reduce_sum(math_ops.square(
        math_ops.real(cplx))) + math_ops.reduce_sum(
            math_ops.square(math_ops.imag(cplx)))
    epsilon = 1e-3
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        inx, list(x.shape), loss, [1], x_init_value=x, delta=epsilon)
self.assertAllClose(jacob_t, jacob_n, rtol=epsilon, atol=epsilon)
