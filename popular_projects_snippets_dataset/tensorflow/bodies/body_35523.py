# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types() + [dtypes.int32, dtypes.int64]:
    maxv = 1.0 if dt.is_floating else 1 << 30
    sampler = self._Sampler(1000, minv=0, maxv=maxv, dtype=dt, use_gpu=True)
    x = sampler()
    y = sampler()
    count = (x == y).sum()
    count_limit = 10
    if dt == dtypes.float16:
        count_limit = 50
    elif dt == dtypes.bfloat16:
        count_limit = 90
    if count >= count_limit:
        print("x = ", x)
        print("y = ", y)
        print("count = ", count)
    self.assertTrue(count < count_limit)
