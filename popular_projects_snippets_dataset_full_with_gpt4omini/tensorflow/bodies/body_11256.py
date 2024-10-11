# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Build a batch matrix and an Operator that should have similar behavior.

    Every operator acts like a (batch) matrix.  This method returns both
    together, and is used by tests.

    Args:
      shapes_info: `OperatorShapesInfo`, encoding shape information about the
        operator.
      dtype:  Numpy dtype.  Data type of returned array/operator.
      use_placeholder:  Python bool.  If True, initialize the operator with a
        placeholder of undefined shape and correct dtype.
      ensure_self_adjoint_and_pd: If `True`,
        construct this operator to be Hermitian Positive Definite, as well
        as ensuring the hints `is_positive_definite` and `is_self_adjoint`
        are set.
        This is useful for testing methods such as `cholesky`.

    Returns:
      operator:  `LinearOperator` subclass instance.
      mat:  `Tensor` representing operator.
    """
# Create a matrix as a numpy array with desired shape/dtype.
# Create a LinearOperator that should have the same behavior as the matrix.
raise NotImplementedError("Not implemented yet.")
