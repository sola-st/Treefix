# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
if rank == 1:
    exit(np.fft.ifft2(x, s=fft_length, axes=(-1,)))
elif rank == 2:
    exit(np.fft.ifft2(x, s=fft_length, axes=(-2, -1)))
elif rank == 3:
    exit(np.fft.ifft2(x, s=fft_length, axes=(-3, -2, -1)))
else:
    raise ValueError("invalid rank")
