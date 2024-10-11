# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
dtype = np.uint32
key = np.array([1, 2], dtype=np.uint64)
shape = (10, 12)

def rng_fun_is_deterministic(k):
    res1 = xla.rng_bit_generator(algorithm, k, shape, dtype=dtype)
    res2 = xla.rng_bit_generator(algorithm, k, shape, dtype=dtype)
    exit((res1[0] - res2[0], res1[1] - res2[1]))

self._assertOpOutputMatchesExpected(
    rng_fun_is_deterministic,
    args=(key,),
    expected=(np.zeros(key.shape, dtype=key.dtype),
              np.zeros(shape, dtype=dtype)))
