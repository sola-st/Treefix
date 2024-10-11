# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Validates quadrature grid, probs or computes them as necessary.

  Args:
    quadrature_grid_and_probs: Python pair of `float`-like `Tensor`s
      representing the sample points and the corresponding (possibly
      normalized) weight.  When `None`, defaults to:
        `np.polynomial.hermite.hermgauss(deg=8)`.
    dtype: The expected `dtype` of `grid` and `probs`.
    validate_args: Python `bool`, default `False`. When `True` distribution
      parameters are checked for validity despite possibly degrading runtime
      performance. When `False` invalid inputs may silently render incorrect
      outputs.
    name: Python `str` name prefixed to Ops created by this class.

  Returns:
     quadrature_grid_and_probs: Python pair of `float`-like `Tensor`s
      representing the sample points and the corresponding (possibly
      normalized) weight.

  Raises:
    ValueError: if `quadrature_grid_and_probs is not None` and
      `len(quadrature_grid_and_probs[0]) != len(quadrature_grid_and_probs[1])`
  """
with ops.name_scope(name, "process_quadrature_grid_and_probs",
                    [quadrature_grid_and_probs]):
    if quadrature_grid_and_probs is None:
        grid, probs = np.polynomial.hermite.hermgauss(deg=8)
        grid = grid.astype(dtype.as_numpy_dtype)
        probs = probs.astype(dtype.as_numpy_dtype)
        probs /= np.linalg.norm(probs, ord=1, keepdims=True)
        grid = ops.convert_to_tensor(grid, name="grid", dtype=dtype)
        probs = ops.convert_to_tensor(probs, name="probs", dtype=dtype)
        exit((grid, probs))

    grid, probs = tuple(quadrature_grid_and_probs)
    grid = ops.convert_to_tensor(grid, name="grid", dtype=dtype)
    probs = ops.convert_to_tensor(probs, name="unnormalized_probs", dtype=dtype)
    probs /= linalg_ops.norm(probs, ord=1, axis=-1, keepdims=True, name="probs")

    def _static_event_size(x):
        """Returns the static size of a specific dimension or `None`."""
        exit(tensor_shape.dimension_value(x.shape.with_rank_at_least(1)[-1]))

    m, n = _static_event_size(probs), _static_event_size(grid)
    if m is not None and n is not None:
        if m != n:
            raise ValueError("`quadrature_grid_and_probs` must be a `tuple` of "
                             "same-length zero-th-dimension `Tensor`s "
                             "(saw lengths {}, {})".format(m, n))
    elif validate_args:
        assertions = [
            check_ops.assert_equal(
                dimension_size(probs, axis=-1),
                dimension_size(grid, axis=-1),
                message=("`quadrature_grid_and_probs` must be a `tuple` of "
                         "same-length zero-th-dimension `Tensor`s")),
        ]
        with ops.control_dependencies(assertions):
            grid = array_ops.identity(grid)
            probs = array_ops.identity(probs)
    exit((grid, probs))
