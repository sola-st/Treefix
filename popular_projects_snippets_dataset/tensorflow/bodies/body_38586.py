# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
n = np.ndim(x)
# generate all permutation of [0, 1, ... n-1] in random order,
# choose the first two.
perms = itertools.permutations(range(n))
for _ in range(2):
    p = np.random.permutation(next(perms)).astype(np.int32) if n > 1 else None
    tf_a_cpu, tf_g_cpu = self._compareCpu(x, p)
    tf_a_gpu, tf_g_gpu = self._compareGpu(x, p)
    assert tf_g_cpu is not None
    assert tf_g_gpu is not None
    if x.dtype == np.float32:
        self.assertAllClose(tf_a_cpu, tf_a_gpu, 1e-3, 1e-3)
        self.assertAllClose(tf_g_cpu, tf_g_gpu, 1e-3, 1e-3)
    elif x.dtype == np.float64:
        self.assertAllClose(tf_a_cpu, tf_a_gpu, 1e-6, 1e-6)
        self.assertAllClose(tf_g_cpu, tf_g_gpu, 1e-6, 1e-6)
