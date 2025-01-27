# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
r"""Initialize an `_BaseLinearOperatorCirculant`.

    Args:
      spectrum:  Shape `[B1,...,Bb] + N` `Tensor`, where `rank(N) in {1, 2, 3}`.
        Allowed dtypes: `float16`, `float32`, `float64`, `complex64`,
        `complex128`.  Type can be different than `input_output_dtype`
      block_depth:  Python integer, either 1, 2, or 3.  Will be 1 for circulant,
        2 for block circulant, and 3 for nested block circulant.
      input_output_dtype: `dtype` for input/output.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  If `spectrum` is real, this will always be true.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix\
            #Extension_for_non_symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      parameters: Python `dict` of parameters used to instantiate this
        `LinearOperator`.
      name:  A name to prepend to all ops created by this class.

    Raises:
      ValueError:  If `block_depth` is not an allowed value.
      TypeError:  If `spectrum` is not an allowed type.
    """

allowed_block_depths = [1, 2, 3]

self._name = name

if block_depth not in allowed_block_depths:
    raise ValueError(
        f"Argument `block_depth` must be one of {allowed_block_depths}. "
        f"Received: {block_depth}.")
self._block_depth = block_depth

with ops.name_scope(name, values=[spectrum]):
    self._spectrum = self._check_spectrum_and_return_tensor(spectrum)

    # Check and auto-set hints.
    if not self.spectrum.dtype.is_complex:
        if is_self_adjoint is False:
            raise ValueError(
                f"A real spectrum always corresponds to a self-adjoint operator. "
                f"Expected argument `is_self_adjoint` to be True when "
                f"`spectrum.dtype.is_complex` = True. "
                f"Received: {is_self_adjoint}.")
        is_self_adjoint = True

    if is_square is False:
        raise ValueError(
            f"A [[nested] block] circulant operator is always square. "
            f"Expected argument `is_square` to be True. Received: {is_square}.")
    is_square = True

    super(_BaseLinearOperatorCirculant, self).__init__(
        dtype=dtypes.as_dtype(input_output_dtype),
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)
