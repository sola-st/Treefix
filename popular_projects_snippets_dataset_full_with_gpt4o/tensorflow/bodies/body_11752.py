# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# Note that we have |X1 x X2| = |X1| ** n * |X2| ** m, where X1 is an m x m
# matrix, and X2 is an n x n matrix. We can iteratively apply this property
# to get the determinant of |X1 x X2 x X3 ...|. If T is the product of the
# domain dimension of all operators, then we have:
# |X1 x X2 x X3 ...| =
#    |X1| ** (T / m) * |X2 x X3 ... | ** m =
#    |X1| ** (T / m) * |X2| ** (m * (T / m) / n) *  ... =
#    |X1| ** (T / m) * |X2| ** (T / n) * | X3 x X4... | ** (m * n)
#    And by doing induction we have product(|X_i| ** (T / dim(X_i))).
total = self.domain_dimension_tensor()
determinant = 1.
for operator in self.operators:
    determinant = determinant * operator.determinant() ** math_ops.cast(
        total / operator.domain_dimension_tensor(),
        dtype=operator.dtype)
exit(determinant)
