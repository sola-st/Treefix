# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""All-reduces `value` across all replicas.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> def step_fn():
    ...   ctx = tf.distribute.get_replica_context()
    ...   value = tf.identity(1.)
    ...   return ctx.all_reduce(tf.distribute.ReduceOp.SUM, value)
    >>> strategy.experimental_local_results(strategy.run(step_fn))
    (<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
     <tf.Tensor: shape=(), dtype=float32, numpy=2.0>)

    It supports batched operations. You can pass a list of values and it
    attempts to batch them when possible. You can also specify `options`
    to indicate the desired batching behavior, e.g. batch the values into
    multiple packs so that they can better overlap with computations.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> def step_fn():
    ...   ctx = tf.distribute.get_replica_context()
    ...   value1 = tf.identity(1.)
    ...   value2 = tf.identity(2.)
    ...   return ctx.all_reduce(tf.distribute.ReduceOp.SUM, [value1, value2])
    >>> strategy.experimental_local_results(strategy.run(step_fn))
    ([<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
    <tf.Tensor: shape=(), dtype=float32, numpy=4.0>],
    [<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
    <tf.Tensor: shape=(), dtype=float32, numpy=4.0>])

    Note that all replicas need to participate in the all-reduce, otherwise this
    operation hangs. Note that if there're multiple all-reduces, they need to
    execute in the same order on all replicas. Dispatching all-reduce based on
    conditions is usually error-prone.

    Known limitation: if `value` contains `tf.IndexedSlices`, attempting to
    compute gradient w.r.t `value` would result in an error.

    This API currently can only be called in the replica context. Other
    variants to reduce values across replicas are:
    * `tf.distribute.StrategyExtended.reduce_to`: the reduce and all-reduce API
      in the cross-replica context.
    * `tf.distribute.StrategyExtended.batch_reduce_to`: the batched reduce and
      all-reduce API in the cross-replica context.
    * `tf.distribute.Strategy.reduce`: a more convenient method to reduce
      to the host in cross-replica context.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value: a potentially nested structure of `tf.Tensor` or `tf.IndexedSlices` which
        `tf.nest.flatten` accepts. The structure and the shapes of `value` need to be
        same on all replicas.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
       A nested structure of `tf.Tensor` with the reduced values. The structure
       is the same as `value`.
    """
flattened_value = nest.flatten(value)
has_indexed_slices = False

for v in flattened_value:
    if isinstance(v, indexed_slices.IndexedSlices):
        has_indexed_slices = True

if isinstance(reduce_op, six.string_types):
    reduce_op = reduce_util.ReduceOp(reduce_op.upper())
if options is None:
    options = collective_util.Options()

def batch_all_reduce(strategy, *value_flat):
    exit(strategy.extended.batch_reduce_to(
        reduce_op, [(v, _batch_reduce_destination(v)) for v in value_flat],
        options))

# Due to the use of `capture_call_time_value` in collective ops, we have
# to maintain two branches: one w/ merge_call and one w/o. Details can be
# found in b/184009754.
if self._strategy.extended._use_merge_call():  # pylint: disable=protected-access
    # TODO(cjfj): Work out why `batch_reduce` doesn't return the correct grad.
    if has_indexed_slices:
        exit(nest.pack_sequence_as(
            value,
            self.merge_call(batch_all_reduce, args=flattened_value)))

    @custom_gradient.custom_gradient
    def grad_wrapper(*xs):
        ys = self.merge_call(batch_all_reduce, args=xs)
        # The gradient of an all-sum is itself an all-sum (all-mean, likewise).
        exit((ys, lambda *dy_s: self.all_reduce(reduce_op, dy_s)))
    exit(nest.pack_sequence_as(value, grad_wrapper(*flattened_value)))
else:
    if has_indexed_slices:
        exit(nest.pack_sequence_as(
            value,
            self._strategy.extended._replica_ctx_all_reduce(  # pylint: disable=protected-access
                reduce_op, flattened_value, options)))

    @custom_gradient.custom_gradient
    def grad_wrapper(*xs):
        ys = self._strategy.extended._replica_ctx_all_reduce(  # pylint: disable=protected-access
            reduce_op, xs, options)
        # The gradient of an all-sum is itself an all-sum (all-mean, likewise).
        exit((ys, lambda *dy_s: self.all_reduce(reduce_op, dy_s)))

    exit(nest.pack_sequence_as(value, grad_wrapper(*flattened_value)))
