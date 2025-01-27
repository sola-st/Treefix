# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
"""Initialize a `LinearOperatorLowRankUpdate`.

    This creates a `LinearOperator` of the form `A = L + U D V^H`, with
    `L` a `LinearOperator`, `U, V` both [batch] matrices, and `D` a [batch]
    diagonal matrix.

    If `L` is non-singular, solves and determinants are available.
    Solves/determinants both involve a solve/determinant of a `K x K` system.
    In the event that L and D are self-adjoint positive-definite, and U = V,
    this can be done using a Cholesky factorization.  The user should set the
    `is_X` matrix property hints, which will trigger the appropriate code path.

    Args:
      base_operator:  Shape `[B1,...,Bb, M, N]`.
      u:  Shape `[B1,...,Bb, M, K]` `Tensor` of same `dtype` as `base_operator`.
        This is `U` above.
      diag_update:  Optional shape `[B1,...,Bb, K]` `Tensor` with same `dtype`
        as `base_operator`.  This is the diagonal of `D` above.
         Defaults to `D` being the identity operator.
      v:  Optional `Tensor` of same `dtype` as `u` and shape `[B1,...,Bb, N, K]`
         Defaults to `v = u`, in which case the perturbation is symmetric.
         If `M != N`, then `v` must be set since the perturbation is not square.
      is_diag_update_positive:  Python `bool`.
        If `True`, expect `diag_update > 0`.
      is_non_singular:  Expect that this operator is non-singular.
        Default is `None`, unless `is_positive_definite` is auto-set to be
        `True` (see below).
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.  Default is `None`, unless `base_operator` is self-adjoint
        and `v = None` (meaning `u=v`), in which case this defaults to `True`.
      is_positive_definite:  Expect that this operator is positive definite.
        Default is `None`, unless `base_operator` is positive-definite
        `v = None` (meaning `u=v`), and `is_diag_update_positive`, in which case
        this defaults to `True`.
        Note that we say an operator is positive definite when the quadratic
        form `x^H A x` has positive real part for all nonzero `x`.
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.

    Raises:
      ValueError:  If `is_X` flags are set in an inconsistent way.
    """
parameters = dict(
    base_operator=base_operator,
    u=u,
    diag_update=diag_update,
    v=v,
    is_diag_update_positive=is_diag_update_positive,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    name=name
)
dtype = base_operator.dtype

if diag_update is not None:
    if is_diag_update_positive and dtype.is_complex:
        logging.warn("Note: setting is_diag_update_positive with a complex "
                     "dtype means that diagonal is real and positive.")

if diag_update is None:
    if is_diag_update_positive is False:
        raise ValueError(
            "Default diagonal is the identity, which is positive.  However, "
            "user set 'is_diag_update_positive' to False.")
    is_diag_update_positive = True

# In this case, we can use a Cholesky decomposition to help us solve/det.
self._use_cholesky = (
    base_operator.is_positive_definite and base_operator.is_self_adjoint
    and is_diag_update_positive
    and v is None)

# Possibly auto-set some characteristic flags from None to True.
# If the Flags were set (by the user) incorrectly to False, then raise.
if base_operator.is_self_adjoint and v is None and not dtype.is_complex:
    if is_self_adjoint is False:
        raise ValueError(
            "A = L + UDU^H, with L self-adjoint and D real diagonal.  Since"
            " UDU^H is self-adjoint, this must be a self-adjoint operator.")
    is_self_adjoint = True

# The condition for using a cholesky is sufficient for SPD, and
# we no weaker choice of these hints leads to SPD.  Therefore,
# the following line reads "if hints indicate SPD..."
if self._use_cholesky:
    if (
        is_positive_definite is False
        or is_self_adjoint is False
        or is_non_singular is False):
        raise ValueError(
            "Arguments imply this is self-adjoint positive-definite operator.")
    is_positive_definite = True
    is_self_adjoint = True

with ops.name_scope(name):

    # Create U and V.
    self._u = linear_operator_util.convert_nonref_to_tensor(u, name="u")
    if v is None:
        self._v = self._u
    else:
        self._v = linear_operator_util.convert_nonref_to_tensor(v, name="v")

    if diag_update is None:
        self._diag_update = None
    else:
        self._diag_update = linear_operator_util.convert_nonref_to_tensor(
            diag_update, name="diag_update")

    # Create base_operator L.
    self._base_operator = base_operator

    super(LinearOperatorLowRankUpdate, self).__init__(
        dtype=self._base_operator.dtype,
        is_non_singular=is_non_singular,
        is_self_adjoint=is_self_adjoint,
        is_positive_definite=is_positive_definite,
        is_square=is_square,
        parameters=parameters,
        name=name)

    # Create the diagonal operator D.
    self._set_diag_operators(diag_update, is_diag_update_positive)
    self._is_diag_update_positive = is_diag_update_positive

    self._check_shapes()
