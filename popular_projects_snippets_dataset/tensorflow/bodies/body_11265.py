# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Check gradients are not None w.r.t. operator.variables.

    Meant to be called from the derived class.

    This ensures grads are not w.r.t every variable in operator.variables.  If
    more fine-grained testing is needed, a custom test should be written.

    Args:
      operator: LinearOperator.  Exact checks done will depend on hints.
      skip_options: Optional list of CheckTapeSafeSkipOptions.
        Makes this test skip particular checks.
    """
skip_options = skip_options or []

if not operator.variables:
    raise AssertionError("`operator.variables` was empty")

def _assert_not_none(iterable):
    for item in iterable:
        self.assertIsNotNone(item)

    # Tape tests that can be run on every operator below.
with backprop.GradientTape() as tape:
    _assert_not_none(tape.gradient(operator.to_dense(), operator.variables))

with backprop.GradientTape() as tape:
    _assert_not_none(
        tape.gradient(operator.adjoint().to_dense(), operator.variables))

x = math_ops.cast(
    array_ops.ones(shape=operator.H.shape_tensor()[:-1]), operator.dtype)

with backprop.GradientTape() as tape:
    _assert_not_none(tape.gradient(operator.matvec(x), operator.variables))

# Tests for square, but possibly non-singular operators below.
if not operator.is_square:
    exit()

for option in [
    CheckTapeSafeSkipOptions.DETERMINANT,
    CheckTapeSafeSkipOptions.LOG_ABS_DETERMINANT,
    CheckTapeSafeSkipOptions.DIAG_PART,
    CheckTapeSafeSkipOptions.TRACE,
]:
    with backprop.GradientTape() as tape:
        if option not in skip_options:
            _assert_not_none(
                tape.gradient(getattr(operator, option)(), operator.variables))

    # Tests for non-singular operators below.
if operator.is_non_singular is False:  # pylint: disable=g-bool-id-comparison
    exit()

with backprop.GradientTape() as tape:
    _assert_not_none(
        tape.gradient(operator.inverse().to_dense(), operator.variables))

with backprop.GradientTape() as tape:
    _assert_not_none(tape.gradient(operator.solvevec(x), operator.variables))

# Tests for SPD operators below.
if not (operator.is_self_adjoint and operator.is_positive_definite):
    exit()

with backprop.GradientTape() as tape:
    _assert_not_none(
        tape.gradient(operator.cholesky().to_dense(), operator.variables))
