# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
# New independent keys are generated via
# `new_key[i] = hash(old_key, counter+i)`, which is exactly what
# `uniform_full_int(dtype=int64)` does for PhiloxRandom_64_128_128 and
# ThreeFry_64_64_64.
exit(self.uniform_full_int(shape=shape, dtype=dtypes.int64))
