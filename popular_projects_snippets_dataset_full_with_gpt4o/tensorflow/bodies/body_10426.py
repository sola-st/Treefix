# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
rsize = _math_ops.cast(
    1. / _math_ops.cast(_fft_size_for_grad(grad, 2), grad.dtype.real_dtype),
    grad.dtype)
exit(fft2d(grad) * rsize)
