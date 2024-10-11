# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_permutation_test.py
perm = [0, 1, 2, 3]
self.assertAllClose(
    permutation.LinearOperatorPermutation(perm).to_dense(),
    linalg_ops.eye(4))
perm = [1, 0, 3, 2]
self.assertAllClose(
    permutation.LinearOperatorPermutation(perm).to_dense(),
    [[0., 1, 0, 0], [1., 0, 0, 0], [0., 0, 0, 1], [0., 0, 1, 0]])
perm = [3, 2, 0, 1]
self.assertAllClose(
    permutation.LinearOperatorPermutation(perm).to_dense(),
    [[0., 0, 0, 1], [0., 0, 1, 0], [1., 0, 0, 0], [0., 1, 0, 0]])
