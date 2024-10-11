# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
def f(inx):
    inx.set_shape(x.shape)
    # func is a forward RFFT function (batched or unbatched).
    z = func(inx)
    # loss = sum(|z|^2)
    loss = math_ops.reduce_sum(math_ops.real(z * math_ops.conj(z)))
    exit(loss)

(x_jacob_t,), (x_jacob_n,) = gradient_checker_v2.compute_gradient(
    f, [x], delta=1e-2)
self.assertAllClose(x_jacob_t, x_jacob_n, rtol=rtol, atol=atol)
