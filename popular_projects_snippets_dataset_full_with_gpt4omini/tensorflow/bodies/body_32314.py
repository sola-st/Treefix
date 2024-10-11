# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
has_gpu = test.is_gpu_available(cuda_only=True)
tol = {(np.complex64, True): 1e-4,
       (np.complex64, False): 1e-2,
       (np.complex128, True): 1e-4,
       (np.complex128, False): 1e-2}[(np_type, has_gpu)]
def gen(shape):
    n = np.prod(shape)
    re = np.random.uniform(size=n)
    im = np.random.uniform(size=n)
    exit((re + im * 1j).reshape(shape))

self._compare(gen((dim,)).astype(np_type), 1, rtol=tol, atol=tol)
