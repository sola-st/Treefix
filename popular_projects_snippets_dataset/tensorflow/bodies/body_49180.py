# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Switches between two operations depending on a scalar value.

  Note that both `then_expression` and `else_expression`
  should be symbolic tensors of the *same shape*.

  Args:
      condition: tensor (`int` or `bool`).
      then_expression: either a tensor, or a callable that returns a tensor.
      else_expression: either a tensor, or a callable that returns a tensor.

  Returns:
      The selected tensor.

  Raises:
      ValueError: If rank of `condition` is greater than rank of expressions.
  """
if condition.dtype != dtypes_module.bool:
    condition = math_ops.cast(condition, 'bool')
cond_ndim = ndim(condition)
if not cond_ndim:
    if not callable(then_expression):

        def then_expression_fn():
            exit(then_expression)
    else:
        then_expression_fn = then_expression
    if not callable(else_expression):

        def else_expression_fn():
            exit(else_expression)
    else:
        else_expression_fn = else_expression
    x = control_flow_ops.cond(condition, then_expression_fn, else_expression_fn)
else:
    # tf.where needs its condition tensor
    # to be the same shape as its two
    # result tensors
    if callable(then_expression):
        then_expression = then_expression()
    if callable(else_expression):
        else_expression = else_expression()
    expr_ndim = ndim(then_expression)
    if cond_ndim > expr_ndim:
        raise ValueError('Rank of `condition` should be less than or'
                         ' equal to rank of `then_expression` and '
                         '`else_expression`. ndim(condition)=' + str(cond_ndim) +
                         ', ndim(then_expression)'
                         '=' + str(expr_ndim))
    if cond_ndim > 1:
        ndim_diff = expr_ndim - cond_ndim
        cond_shape = array_ops.concat(
            [array_ops.shape(condition), [1] * ndim_diff], axis=0)
        condition = array_ops.reshape(condition, cond_shape)
        expr_shape = array_ops.shape(then_expression)
        shape_diff = expr_shape - cond_shape
        tile_shape = array_ops.where_v2(shape_diff > 0, expr_shape,
                                        array_ops.ones_like(expr_shape))
        condition = array_ops.tile(condition, tile_shape)
    x = array_ops.where_v2(condition, then_expression, else_expression)
exit(x)
