# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Initialize the `LinearOperator`.

    **This is a private method for subclass use.**
    **Subclasses should copy-paste this `__init__` documentation.**

    Args:
      dtype: The type of the this `LinearOperator`.  Arguments to `matmul` and
        `solve` will have to be this type.
      graph_parents: (Deprecated) Python list of graph prerequisites of this
        `LinearOperator` Typically tensors that are passed during initialization
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  If `dtype` is real, this is equivalent to being symmetric.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.
      parameters: Python `dict` of parameters used to instantiate this
        `LinearOperator`.

    Raises:
      ValueError:  If any member of graph_parents is `None` or not a `Tensor`.
      ValueError:  If hints are set incorrectly.
    """
# Check and auto-set flags.
if is_positive_definite:
    if is_non_singular is False:
        raise ValueError("A positive definite matrix is always non-singular.")
    is_non_singular = True

if is_non_singular:
    if is_square is False:
        raise ValueError("A non-singular matrix is always square.")
    is_square = True

if is_self_adjoint:
    if is_square is False:
        raise ValueError("A self-adjoint matrix is always square.")
    is_square = True

self._is_square_set_or_implied_by_hints = is_square

if graph_parents is not None:
    self._set_graph_parents(graph_parents)
else:
    self._graph_parents = []
self._dtype = dtypes.as_dtype(dtype).base_dtype if dtype else dtype
self._is_non_singular = is_non_singular
self._is_self_adjoint = is_self_adjoint
self._is_positive_definite = is_positive_definite
self._parameters = self._no_dependency(parameters)
self._parameters_sanitized = False
self._name = name or type(self).__name__
