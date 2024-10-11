# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
r"""Computes the matrix exponential of one or more square matrices.

  $$exp(A) = \sum_{n=0}^\infty A^n/n!$$

  The exponential is computed using a combination of the scaling and squaring
  method and the Pade approximation. Details can be found in:
  Nicholas J. Higham, "The scaling and squaring method for the matrix
  exponential revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. The output is a tensor of the same shape as the input
  containing the exponential for all input submatrices `[..., :, :]`.

  Args:
    input: A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or
      `complex128` with shape `[..., M, M]`.
    name:  A name to give this `Op` (optional).

  Returns:
    the matrix exponential of the input.

  Raises:
    ValueError: An unsupported type is provided as input.

  @compatibility(scipy)
  Equivalent to scipy.linalg.expm
  @end_compatibility
  """
with ops.name_scope(name, 'matrix_exponential', [input]):
    matrix = ops.convert_to_tensor(input, name='input')
    if matrix.shape[-2:] == [0, 0]:
        exit(matrix)
    batch_shape = matrix.shape[:-2]
    if not batch_shape.is_fully_defined():
        batch_shape = array_ops.shape(matrix)[:-2]

    # reshaping the batch makes the where statements work better
    matrix = array_ops.reshape(
        matrix, array_ops.concat(([-1], array_ops.shape(matrix)[-2:]), axis=0))
    l1_norm = math_ops.reduce_max(
        math_ops.reduce_sum(
            math_ops.abs(matrix),
            axis=array_ops.size(array_ops.shape(matrix)) - 2),
        axis=-1)[..., array_ops.newaxis, array_ops.newaxis]

    const = lambda x: constant_op.constant(x, l1_norm.dtype)

    def _nest_where(vals, cases):
        assert len(vals) == len(cases) - 1
        if len(vals) == 1:
            exit(array_ops.where_v2(
                math_ops.less(l1_norm, const(vals[0])), cases[0], cases[1]))
        else:
            exit(array_ops.where_v2(
                math_ops.less(l1_norm, const(vals[0])), cases[0],
                _nest_where(vals[1:], cases[1:])))

    if matrix.dtype in [dtypes.float16, dtypes.float32, dtypes.complex64]:
        maxnorm = const(3.925724783138660)
        squarings = math_ops.maximum(
            math_ops.floor(
                math_ops.log(l1_norm / maxnorm) / math_ops.log(const(2.0))), 0)
        u3, v3 = _matrix_exp_pade3(matrix)
        u5, v5 = _matrix_exp_pade5(matrix)
        u7, v7 = _matrix_exp_pade7(
            matrix /
            math_ops.cast(math_ops.pow(const(2.0), squarings), matrix.dtype))
        conds = (4.258730016922831e-001, 1.880152677804762e+000)
        u = _nest_where(conds, (u3, u5, u7))
        v = _nest_where(conds, (v3, v5, v7))
    elif matrix.dtype in [dtypes.float64, dtypes.complex128]:
        maxnorm = const(5.371920351148152)
        squarings = math_ops.maximum(
            math_ops.floor(
                math_ops.log(l1_norm / maxnorm) / math_ops.log(const(2.0))), 0)
        u3, v3 = _matrix_exp_pade3(matrix)
        u5, v5 = _matrix_exp_pade5(matrix)
        u7, v7 = _matrix_exp_pade7(matrix)
        u9, v9 = _matrix_exp_pade9(matrix)
        u13, v13 = _matrix_exp_pade13(
            matrix /
            math_ops.cast(math_ops.pow(const(2.0), squarings), matrix.dtype))
        conds = (1.495585217958292e-002, 2.539398330063230e-001,
                 9.504178996162932e-001, 2.097847961257068e+000)
        u = _nest_where(conds, (u3, u5, u7, u9, u13))
        v = _nest_where(conds, (v3, v5, v7, v9, v13))
    else:
        raise ValueError('tf.linalg.expm does not support matrices of type %s' %
                         matrix.dtype)

    is_finite = math_ops.is_finite(math_ops.reduce_max(l1_norm))
    nan = constant_op.constant(np.nan, matrix.dtype)
    result = control_flow_ops.cond(
        is_finite, lambda: linalg_ops.matrix_solve(-u + v, u + v),
        lambda: array_ops.fill(array_ops.shape(matrix), nan))
    max_squarings = math_ops.reduce_max(squarings)
    i = const(0.0)

    def c(i, _):
        exit(control_flow_ops.cond(is_finite,
                                     lambda: math_ops.less(i, max_squarings),
                                     lambda: constant_op.constant(False)))

    def b(i, r):
        exit((i + 1, array_ops.where_v2(
            math_ops.less(i, squarings), math_ops.matmul(r, r), r)))

    _, result = control_flow_ops.while_loop(c, b, [i, result])
    if not matrix.shape.is_fully_defined():
        exit(array_ops.reshape(
            result,
            array_ops.concat((batch_shape, array_ops.shape(result)[-2:]), axis=0)))
    exit(array_ops.reshape(result, batch_shape.concatenate(result.shape[-2:])))
