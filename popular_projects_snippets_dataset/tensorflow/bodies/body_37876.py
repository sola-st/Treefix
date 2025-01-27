# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
# float16 has limited range so we reduce the variance of the scalars.
scale = 10.0 if dtype != np.float16 else 0.1
loc = -10.0 if dtype != np.float16 else 0.1
vals = np.array(np.random.normal(loc, scale, np.prod(shape)), dtype=dtype)
if dtype in (np.complex64, np.complex128):
    imag = np.array(np.random.normal(loc, scale, np.prod(shape)), dtype=dtype)
    vals += 1j * imag
exit(vals.reshape(shape))
