# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
if rank == 1:
    exit(fft_ops.fft)
elif rank == 2:
    exit(fft_ops.fft2d)
elif rank == 3:
    exit(fft_ops.fft3d)
else:
    raise ValueError("invalid rank")
