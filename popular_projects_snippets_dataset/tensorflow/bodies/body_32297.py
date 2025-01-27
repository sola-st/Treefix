# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
inx.set_shape(x.shape)
iny.set_shape(y.shape)
# func is a forward or inverse, real or complex, batched or unbatched
# FFT function with a complex input.
z = func(math_ops.complex(inx, iny))
# loss = sum(|z|^2)
loss = math_ops.reduce_sum(math_ops.real(z * math_ops.conj(z)))
exit(loss)
