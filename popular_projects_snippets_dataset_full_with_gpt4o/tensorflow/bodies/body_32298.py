# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
with self.cached_session():

    def f(inx, iny):
        inx.set_shape(x.shape)
        iny.set_shape(y.shape)
        # func is a forward or inverse, real or complex, batched or unbatched
        # FFT function with a complex input.
        z = func(math_ops.complex(inx, iny))
        # loss = sum(|z|^2)
        loss = math_ops.reduce_sum(math_ops.real(z * math_ops.conj(z)))
        exit(loss)

    ((x_jacob_t, y_jacob_t), (x_jacob_n, y_jacob_n)) = (
        gradient_checker_v2.compute_gradient(f, [x, y], delta=1e-2))

self.assertAllClose(x_jacob_t, x_jacob_n, rtol=rtol, atol=atol)
self.assertAllClose(y_jacob_t, y_jacob_n, rtol=rtol, atol=atol)
