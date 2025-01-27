# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Combine multiple `reduce_to` calls into one for faster execution.

    Similar to `reduce_to`, but accepts a list of (value, destinations) pairs.
    It's more efficient than reduce each value separately.

    This API currently can only be called in cross-replica context. Other
    variants to reduce values across replicas are:
    * `tf.distribute.StrategyExtended.reduce_to`: the non-batch version of
      this API.
    * `tf.distribute.ReplicaContext.all_reduce`: the counterpart of this API
      in replica context. It supports both batched and non-batched all-reduce.
    * `tf.distribute.Strategy.reduce`: a more convenient method to reduce
      to the host in cross-replica context.

    See `reduce_to` for more information.

    >>> @tf.function
    ... def step_fn(var):
    ...
    ...   def merge_fn(strategy, value, var):
    ...     # All-reduce the value. Note that `value` here is a
    ...     # `tf.distribute.DistributedValues`.
    ...     reduced = strategy.extended.batch_reduce_to(
    ...         tf.distribute.ReduceOp.SUM, [(value, var)])[0]
    ...     strategy.extended.update(var, lambda var, value: var.assign(value),
    ...         args=(reduced,))
    ...
    ...   value = tf.identity(1.)
    ...   tf.distribute.get_replica_context().merge_call(merge_fn,
    ...     args=(value, var))
    >>>
    >>> def run(strategy):
    ...   with strategy.scope():
    ...     v = tf.Variable(0.)
    ...     strategy.run(step_fn, args=(v,))
    ...     return v
    >>>
    >>> run(tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"]))
    MirroredVariable:{
      0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>,
      1: <tf.Variable 'Variable/replica_1:0' shape=() dtype=float32, numpy=2.0>
    }
    >>> run(tf.distribute.experimental.CentralStorageStrategy(
    ...     compute_devices=["GPU:0", "GPU:1"], parameter_device="CPU:0"))
    <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>
    >>> run(tf.distribute.OneDeviceStrategy("GPU:0"))
    <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value_destination_pairs: a sequence of (value, destinations) pairs. See
        `tf.distribute.Strategy.reduce_to` for descriptions.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
      A list of reduced values, one per pair in `value_destination_pairs`.
    """
if options is None:
    options = collective_util.Options()
_require_cross_replica_or_default_context_extended(self)
assert not isinstance(reduce_op, variable_scope.VariableAggregation)
if isinstance(reduce_op, six.string_types):
    reduce_op = reduce_util.ReduceOp(reduce_op.upper())
exit(self._batch_reduce_to(reduce_op, value_destination_pairs, options))
