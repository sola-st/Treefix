# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# pylint: disable=line-too-long, protected-access
"""Gather `value` across replicas along `axis` to the current device.

    Given a `tf.distribute.DistributedValues` or `tf.Tensor`-like
    object `value`, this API gathers and concatenates `value` across replicas
    along the `axis`-th dimension. The result is copied to the "current" device,
    which would typically be the CPU of the worker on which the program is
    running. For `tf.distribute.TPUStrategy`, it is the first TPU host. For
    multi-client `tf.distribute.MultiWorkerMirroredStrategy`, this is the CPU of
    each worker.

    This API can only be called in the cross-replica context. For a counterpart
    in the replica context, see `tf.distribute.ReplicaContext.all_gather`.

    Note: For all strategies except `tf.distribute.TPUStrategy`, the input
    `value` on different replicas must have the same rank, and their shapes must
    be the same in all dimensions except the `axis`-th dimension. In other
    words, their shapes cannot be different in a dimension `d` where `d` does
    not equal to the `axis` argument. For example, given a
    `tf.distribute.DistributedValues` with component tensors of shape
    `(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
    `gather(..., axis=1, ...)` on it, but not `gather(..., axis=0, ...)` or
    `gather(..., axis=2, ...)`. However, for `tf.distribute.TPUStrategy.gather`,
    all tensors must have exactly the same rank and same shape.

    Note: Given a `tf.distribute.DistributedValues` `value`, its component
    tensors must have a non-zero rank. Otherwise, consider using
    `tf.expand_dims` before gathering them.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> # A DistributedValues with component tensor of shape (2, 1) on each replica
    ... distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(tf.constant([[1], [2]])))
    >>> @tf.function
    ... def run():
    ...   return strategy.gather(distributed_values, axis=0)
    >>> run()
    <tf.Tensor: shape=(4, 1), dtype=int32, numpy=
    array([[1],
           [2],
           [1],
           [2]], dtype=int32)>


    Consider the following example for more combinations:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2", "GPU:3"])
    >>> single_tensor = tf.reshape(tf.range(6), shape=(1,2,3))
    >>> distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(single_tensor))
    >>> @tf.function
    ... def run(axis):
    ...   return strategy.gather(distributed_values, axis=axis)
    >>> axis=0
    >>> run(axis)
    <tf.Tensor: shape=(4, 2, 3), dtype=int32, numpy=
    array([[[0, 1, 2],
            [3, 4, 5]],
           [[0, 1, 2],
            [3, 4, 5]],
           [[0, 1, 2],
            [3, 4, 5]],
           [[0, 1, 2],
            [3, 4, 5]]], dtype=int32)>
    >>> axis=1
    >>> run(axis)
    <tf.Tensor: shape=(1, 8, 3), dtype=int32, numpy=
    array([[[0, 1, 2],
            [3, 4, 5],
            [0, 1, 2],
            [3, 4, 5],
            [0, 1, 2],
            [3, 4, 5],
            [0, 1, 2],
            [3, 4, 5]]], dtype=int32)>
    >>> axis=2
    >>> run(axis)
    <tf.Tensor: shape=(1, 2, 12), dtype=int32, numpy=
    array([[[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
            [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]]], dtype=int32)>


    Args:
      value: a `tf.distribute.DistributedValues` instance, e.g. returned by
        `Strategy.run`, to be combined into a single tensor. It can also be a
        regular tensor when used with `tf.distribute.OneDeviceStrategy` or the
        default strategy. The tensors that constitute the DistributedValues
        can only be dense tensors with non-zero rank, NOT a `tf.IndexedSlices`.
      axis: 0-D int32 Tensor. Dimension along which to gather. Must be in the
        range [0, rank(value)).

    Returns:
       A `Tensor` that's the concatenation of `value` across replicas along
       `axis` dimension.
    """
# pylint: enable=line-too-long
error_message = ("tf.distribute.Strategy.gather method requires "
                 "cross-replica context, use "
                 "get_replica_context().all_gather() instead")
_require_cross_replica_or_default_context_extended(self._extended,
                                                   error_message)
dst = device_util.current(
) or self._extended._default_device or "/device:CPU:0"
if isinstance(value, indexed_slices.IndexedSlices):
    raise NotImplementedError("gather does not support IndexedSlices")
exit(self._extended._local_results(
    self._extended._gather_to(value, dst, axis))[0])
