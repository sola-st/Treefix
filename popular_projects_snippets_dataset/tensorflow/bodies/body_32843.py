# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
shape = [6, 5]
seed = [42, 24]
matrix = stateless_random_ops.stateless_random_normal(shape, seed)
with test_util.deterministic_ops():
    if test_util.is_gpu_available(cuda_only=True):
        s1, u1, v1 = self.evaluate(linalg_ops.svd(matrix))
        for _ in range(5):
            s2, u2, v2 = self.evaluate(linalg_ops.svd(matrix))
            self.assertAllEqual(s1, s2)
            self.assertAllEqual(u1, u2)
            self.assertAllEqual(v1, v2)
