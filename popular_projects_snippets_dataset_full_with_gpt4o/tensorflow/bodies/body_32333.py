# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
def gen_real(shape):
    n = np.prod(shape)
    re = np.random.uniform(size=n)
    ret = re.reshape(shape)
    exit(ret)

def gen_complex(shape):
    n = np.prod(shape)
    re = np.random.uniform(size=n)
    im = np.random.uniform(size=n)
    ret = (re + im * 1j).reshape(shape)
    exit(ret)
np_ctype = np.complex64 if np_rtype == np.float32 else np.complex128
tol = 1e-4 if np_rtype == np.float32 else 1e-5
dims = rank + extra_dims
r2c = gen_real((size,) * dims)
inner_dim = size // 2 + 1
fft_length = (size,) * rank
self._compare_forward(
    r2c.astype(np_rtype), rank, fft_length, rtol=tol, atol=tol)
complex_dims = (size,) * (dims - 1) + (inner_dim,)
c2r = gen_complex(complex_dims)
c2r = self._generate_valid_irfft_input(c2r, np_ctype, r2c, np_rtype, rank,
                                       fft_length)
self._compare_backward(c2r, rank, fft_length, rtol=tol, atol=tol)
