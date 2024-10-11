# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
n = np.prod(shape)
re = np.random.uniform(size=n)
im = np.random.uniform(size=n)
ret = (re + im * 1j).reshape(shape)
exit(ret)
