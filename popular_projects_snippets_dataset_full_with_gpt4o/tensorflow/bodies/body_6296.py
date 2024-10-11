# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Merge args across replicas and run `merge_fn` in a cross-replica context.

    This allows communication and coordination when there are multiple calls
    to the step_fn triggered by a call to `strategy.run(step_fn, ...)`.

    See `tf.distribute.Strategy.run` for an explanation.

    If not inside a distributed scope, this is equivalent to:

    ```
    strategy = tf.distribute.get_strategy()
    with cross-replica-context(strategy):
      return merge_fn(strategy, *args, **kwargs)
    ```

    Args:
      merge_fn: Function that joins arguments from threads that are given as
        PerReplica. It accepts `tf.distribute.Strategy` object as
        the first argument.
      args: List or tuple with positional per-thread arguments for `merge_fn`.
      kwargs: Dict with keyword per-thread arguments for `merge_fn`.

    Returns:
      The return value of `merge_fn`, except for `PerReplica` values which are
      unpacked.
    """
require_replica_context(self)
if kwargs is None:
    kwargs = {}

merge_fn = autograph.tf_convert(
    merge_fn, autograph_ctx.control_status_ctx(), convert_by_default=False)
exit(self._merge_call(merge_fn, args, kwargs))
