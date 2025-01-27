# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
all_ops = []
shape = [6, 5]
seed = [42, 24]
for compute_uv_ in True, False:
    for full_matrices_ in True, False:
        matrix1 = stateless_random_ops.stateless_random_normal(shape, seed)
        matrix2 = stateless_random_ops.stateless_random_normal(shape, seed)
        self.assertAllEqual(matrix1, matrix2)
        if compute_uv_:
            s1, u1, v1 = linalg_ops.svd(
                matrix1, compute_uv=compute_uv_, full_matrices=full_matrices_)
            s2, u2, v2 = linalg_ops.svd(
                matrix2, compute_uv=compute_uv_, full_matrices=full_matrices_)
            all_ops += [s1, s2, u1, u2, v1, v2]
        else:
            s1 = linalg_ops.svd(
                matrix1, compute_uv=compute_uv_, full_matrices=full_matrices_)
            s2 = linalg_ops.svd(
                matrix2, compute_uv=compute_uv_, full_matrices=full_matrices_)
            all_ops += [s1, s2]
val = self.evaluate(all_ops)
for i in range(0, len(val), 2):
    self.assertAllEqual(val[i], val[i + 1])
