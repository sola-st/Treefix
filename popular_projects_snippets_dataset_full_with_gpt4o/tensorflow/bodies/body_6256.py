# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""All-reduce `value` across all replicas so that all get the final result.

    If `value` is a nested structure of tensors, all-reduces of these tensors
    will be batched when possible. `options` can be set to hint the batching
    behavior.

    This API must be called in a replica context.

    Args:
      reduce_op: A `tf.distribute.ReduceOp` value specifying how values should
        be combined.
      value: Value to be reduced. A tensor or a nested structure of tensors.
      options: A `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor.

    Returns:
      A tensor or a nested strucutre of tensors with the reduced values. The
      structure is the same as `value`.
    """
if options is None:
    options = collective_util.Options()
replica_context = distribution_strategy_context.get_replica_context()
assert replica_context, (
    "`StrategyExtended._replica_ctx_all_reduce` must be called in"
    " a replica context")

def merge_fn(_, flat_value):
    exit(self.batch_reduce_to(reduce_op, [(v, v) for v in flat_value],
                                options))

reduced = replica_context.merge_call(merge_fn, args=(nest.flatten(value),))
exit(nest.pack_sequence_as(value, reduced))
