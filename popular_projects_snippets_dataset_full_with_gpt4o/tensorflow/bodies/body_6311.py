# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Run `fn` to update `var` with `args` and `kwargs` in replica context.

    `tf.distribute.ReplicaContext.update` takes a (distributed) variable `var`
    to be updated, an update function `fn`, and `args` and `kwargs` for `fn`.
    `fn` applies to each component variable of `var` with corresponding input
    values from `args` and `kwargs`.

    Example usage:

    >>> strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1']) # 2 replicas
    >>> with strategy.scope():
    ...   distributed_variable = tf.Variable(5.0)
    >>> distributed_variable
    MirroredVariable:{
      0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=5.0>,
      1: <tf.Variable 'Variable/replica_1:0' shape=() dtype=float32, numpy=5.0>
    }
    >>> def replica_fn(v):
    ...   value = tf.identity(1.0)
    ...   replica_context = tf.distribute.get_replica_context()
    ...   update_fn = lambda var, value: var.assign(value)
    ...   replica_context._update(v, update_fn, args=(value,))
    >>> strategy.run(replica_fn, args=(distributed_variable,))
    >>> distributed_variable
    MirroredVariable:{
      0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>,
      1: <tf.Variable 'Variable/replica_1:0' shape=() dtype=float32, numpy=1.0>
    }

    This API must be called in a replica context.

    Note that if `var` is a MirroredVariable (i.e., the type of variable created
    under the scope of a synchronous strategy, and is synchronized on-write, see
    `tf.VariableSynchronization` for more information) and `args`/`kwargs`
    contains different values for different replicas, `var` will be dangerously
    out of synchronization. Thus we recommend using `variable.assign(value)` as
    long as you can, which under the hood aggregates the updates and guarantees
    the synchronization. The case where you actually want this API instead of
    `variable.assign(value)` is that before assigning `value` to the `variable`,
    you'd like to conduct some pre-`assign` computation colocated with the
    variable devices (i.e. where variables reside, for MirroredStrategy they are
    the same as the compute device, for ParameterServerStrategy they refer to
    parameter servers). E.g.,

    ```python
    strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1']) # 2 replicas
    with strategy.scope():
      v = tf.Variable(5.0, aggregation=tf.VariableAggregation.SUM)
    def replica_fn(inputs):
      value = computation(inputs)
      replica_context = tf.distribute.get_replica_context()
      reduced_value = replica_context.all_reduce(value)

      def update_fn(var, value):
        # this computation will colocate with `var`'s device
        updated_value = post_reduce_pre_update_computation(value)
        var.assign(value)

      replica_context._update(v, update_fn, args=(reduced_value,))

    strategy.run(replica_fn, args=(inputs,))
    ```

    This code snippet is consistent across all strategies. If you directly
    compute and use `assign` in the replica context instead of wrapping it with
    `update`, for strategies with fewer variable devices than compute devices
    (e.g., parameter server strategy, usually), the
    `post_reduce_pre_update_computation` will happen
    N==number_of_compute_devices times which is less performant.


    Args:
      var: Variable, possibly distributed to multiple devices, to operate on.
      fn: Function to call. Should take the variable as the first argument.
      args: Tuple or list. Additional positional arguments to pass to `fn()`.
      kwargs: Dict with keyword arguments to pass to `fn()`.
      group: Boolean. Defaults to True. Most strategies enter a merge_call to
      conduct update in cross-replica context, and group=True guarantees updates
      on all replicas is executed.

    Returns:
      The return value of `fn` for the local replica.
    """
if kwargs is None:
    kwargs = {}
exit(self._strategy.extended._replica_ctx_update(var, fn, args=args, kwargs=kwargs, group=group))  # pylint: disable=protected-access
