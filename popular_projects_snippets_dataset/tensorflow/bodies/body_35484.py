# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
"""CSE = constant subexpression eliminator.

    SetIsStateful() should prevent two identical random ops from getting
    merged.
    """
for dtype in dtypes.float16, dtypes.float32, dtypes.float64:
    with self.cached_session():
        rnd1 = random_ops.random_gamma([24], 2.0, dtype=dtype)
        rnd2 = random_ops.random_gamma([24], 2.0, dtype=dtype)
        diff = rnd2 - rnd1
        self.assertGreater(np.linalg.norm(diff.eval()), 0.1)
