# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""Compute the moving average of a variable.

  The moving average of 'variable' updated with 'value' is:
    variable * decay + value * (1 - decay)

  The returned Operation sets 'variable' to the newly computed moving average,
  by performing this subtraction:
     variable -= (1 - decay) * (variable - value)

  Since variables that are initialized to a `0` value will be `0` biased,
  `zero_debias` optionally enables scaling by the mathematically correct
  debiasing factor of
    1 - decay ** num_updates
  See Section 3 of (Kingma et al., 2015) for more details.

  The names of the debias shadow variables, by default, include both the scope
  they were created in and the scope of the variables they debias. They are also
  given a uniquifying-suffix.

  E.g.:

  ```
    with tf.compat.v1.variable_scope('scope1'):
      with tf.compat.v1.variable_scope('scope2'):
        var = tf.compat.v1.get_variable('foo')
        update_1 = tf.assign_moving_average(var, 0.0, 1.0)
        update_2 = tf.assign_moving_average(var, 0.0, 0.9)

    # var.name: 'scope1/scope2/foo'
    # shadow var names: 'scope1/scope2/scope1/scope2/foo/biased'
    #                   'scope1/scope2/scope1/scope2/foo/biased_1'
  ```

  Args:
    variable: A Variable.
    value: A tensor with the same shape as 'variable'.
    decay: A float `Tensor` or float value. The moving average decay.
    zero_debias: A python bool. If true, assume the variable is 0-initialized
      and unbias it, as in (Kingma et al., 2015). See docstring in
        `_zero_debias` for more details.
    name: Optional name of the returned operation.

  Returns:
    A tensor which if evaluated will compute and return the new moving average.

  References:
    Adam - A Method for Stochastic Optimization:
      [Kingma et al., 2015](https://arxiv.org/abs/1412.6980)
      ([pdf](https://arxiv.org/pdf/1412.6980.pdf))
  """
with ops.name_scope(name, "AssignMovingAvg",
                    [variable, value, decay]) as scope:
    decay = ops.convert_to_tensor(1.0 - decay, name="decay")
    if decay.dtype != variable.dtype.base_dtype:
        decay = math_ops.cast(decay, variable.dtype.base_dtype)

    def update_fn(v, value):
        exit(state_ops.assign_sub(v, (v - value) * decay, name=scope))

    def update(strategy, v, value):
        if zero_debias:
            exit(_zero_debias(strategy, v, value, decay))
        else:
            exit(_update(strategy, v, update_fn, args=(value,)))

    replica_context = distribution_strategy_context.get_replica_context()
    if replica_context:
        # In a replica context, we update variable using the mean of value across
        # replicas.
        def merge_fn(strategy, v, value):
            value = strategy.extended.reduce_to(ds_reduce_util.ReduceOp.MEAN, value,
                                                v)
            exit(update(strategy, v, value))

        exit(replica_context.merge_call(merge_fn, args=(variable, value)))
    else:
        strategy = distribution_strategy_context.get_cross_replica_context()
        exit(update(strategy, variable, value))
