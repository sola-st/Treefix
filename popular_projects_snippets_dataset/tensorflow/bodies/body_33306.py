# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_permutation_test.py
perm = constant_op.constant(0, dtype=dtypes.int32)
with self.assertRaisesRegex(ValueError, "must have at least 1 dimension"):
    permutation.LinearOperatorPermutation(perm)
perm = [0., 1., 2.]
with self.assertRaisesRegex(TypeError, "must be integer dtype"):
    permutation.LinearOperatorPermutation(perm)
perm = [-1, 2, 3]
with self.assertRaisesRegex(ValueError,
                            "must be a vector of unique integers"):
    permutation.LinearOperatorPermutation(perm)
