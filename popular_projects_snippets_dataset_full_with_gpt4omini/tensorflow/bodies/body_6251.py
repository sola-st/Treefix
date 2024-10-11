# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Combine (via e.g. sum or mean) values across replicas.

    `reduce_to` aggregates `tf.distribute.DistributedValues` and distributed
    variables. It supports both dense values and `tf.IndexedSlices`.

    This API currently can only be called in cross-replica context. Other
    variants to reduce values across replicas are:
    * `tf.distribute.StrategyExtended.batch_reduce_to`: the batch version of
      this API.
    * `tf.distribute.ReplicaContext.all_reduce`: the counterpart of this API
      in replica context. It supports both batched and non-batched all-reduce.
    * `tf.distribute.Strategy.reduce`: a more convenient method to reduce
      to the host in cross-replica context.

    `destinations` specifies where to reduce the value to, e.g. "GPU:0". You can
    also pass in a `Tensor`, and the destinations will be the device of that
    tensor. For all-reduce, pass the same to `value` and `destinations`.

    It can be used in `tf.distribute.ReplicaContext.merge_call` to write code
    that works for all `tf.distribute.Strategy`.

    >>> @tf.function
    ... def step_fn(var):
    ...
    ...   def merge_fn(strategy, value, var):
    ...     # All-reduce the value. Note that `value` here is a
    ...     # `tf.distribute.DistributedValues`.
    ...     reduced = strategy.extended.reduce_to(tf.distribute.ReduceOp.SUM,
    ...         value, destinations=var)
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
      value: a `tf.distribute.DistributedValues`, or a `tf.Tensor` like object.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to reduce to. To perform an all-reduce, pass the same to `value` and
        `destinations`. Note that if it's a `tf.Variable`, the value is reduced
        to the devices of that variable, and this method doesn't update the
        variable.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
      A tensor or value reduced to `destinations`.
    """
if options is None:
    options = collective_util.Options()
_require_cross_replica_or_default_context_extended(self)
assert not isinstance(destinations, (list, tuple))
assert not isinstance(reduce_op, variable_scope.VariableAggregation)
if isinstance(reduce_op, six.string_types):
    reduce_op = reduce_util.ReduceOp(reduce_op.upper())
assert (reduce_op == reduce_util.ReduceOp.SUM or
        reduce_op == reduce_util.ReduceOp.MEAN)
exit(self._reduce_to(reduce_op, value, destinations, options))
