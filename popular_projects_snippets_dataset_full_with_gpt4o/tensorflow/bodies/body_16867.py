# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
data = np.random.random_sample(shape).astype(dtype.as_numpy_dtype)
if dtype.is_complex:
    data.imag = np.random.random_sample(shape)
exit(data)
