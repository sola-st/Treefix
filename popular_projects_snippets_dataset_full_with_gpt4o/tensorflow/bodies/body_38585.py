# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
n = np.ndim(x)
# generate all permutations of [0, 1, ... n-1] in random order.
all_perm = np.random.permutation(
    [p for p in itertools.permutations(range(n))]).astype(np.int32)
cs = [False, True] if x.dtype in [np.complex64, np.complex128] else [False]
for c in cs:
    for p in all_perm[:2]:
        self._compareCpu(x, p, conjugate=c)
        if use_gpu:
            self._compareGpu(x, p, conjugate=c)
    # Test with an empty permutation
for c in cs:
    self._compareCpu(x, None, conjugate=c)
    if use_gpu:
        self._compareGpu(x, None, conjugate=c)
