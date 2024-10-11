# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
size = _math_ops.cast(_fft_size_for_grad(grad, 3), grad.dtype)
exit(ifft3d(grad) * size)
