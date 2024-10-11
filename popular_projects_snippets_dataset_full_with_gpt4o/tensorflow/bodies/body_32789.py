# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = array_ops.placeholder_with_default(
    input=np.ones((2, 2)), shape=None)
operator = LinearOperatorMatmulSolve(matrix)
if not context.executing_eagerly():
    # Eager mode will read in the default value, and discover the answer is
    # True.  Graph mode must rely on the hint, since the placeholder has
    # shape=None...the hint is, by default, None.
    self.assertEqual(None, operator.is_square)

# Set to True
operator = LinearOperatorMatmulSolve(matrix, is_square=True)
self.assertTrue(operator.is_square)
