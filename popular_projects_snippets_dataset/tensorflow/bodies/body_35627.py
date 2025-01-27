# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
"""CSE = constant subexpression eliminator.

    SetIsStateful() should prevent two identical random ops from getting
    merged.
    """
for dtype in dtypes.float16, dtypes.float32, dtypes.float64:
    with self.cached_session():
        rnd1 = random_ops.random_poisson(2.0, [24], dtype=dtype)
        rnd2 = random_ops.random_poisson(2.0, [24], dtype=dtype)
        diff = rnd2 - rnd1
        # Since these are all positive integers, the norm will
        # be at least 1 if they are different.
        self.assertGreaterEqual(np.linalg.norm(diff.eval()), 1)
