# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""All-gathers `value` across all replicas along `axis`.

    Note: An `all_gather` method can only be called in replica context. For
    a cross-replica context counterpart, see `tf.distribute.Strategy.gather`.
    All replicas need to participate in the all-gather, otherwise this
    operation hangs. So if `all_gather` is called in any replica, it must be
    called in all replicas.

    Note: If there are multiple `all_gather` calls, they need to be executed in
    the same order on all replicas. Dispatching `all_gather` based on conditions
    is usually error-prone.

    For all strategies except `tf.distribute.TPUStrategy`, the input
    `value` on different replicas must have the same rank, and their shapes must
    be the same in all dimensions except the `axis`-th dimension. In other
    words, their shapes cannot be different in a dimension `d` where `d` does
    not equal to the `axis` argument. For example, given a
    `tf.distribute.DistributedValues` with component tensors of shape
    `(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
    `all_gather(..., axis=1, ...)` on it, but not `all_gather(..., axis=0, ...)`
    or `all_gather(..., axis=2, ...)`. However, with
    `tf.distribute.TPUStrategy`, all tensors must have exactly the same rank and
    same shape.

    Note: The input `value` must have a non-zero rank. Otherwise, consider using
    `tf.expand_dims` before gathering them.

    You can pass in a single tensor to all-gather:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> @tf.function
    ... def gather_value():
    ...   ctx = tf.distribute.get_replica_context()
    ...   local_value = tf.constant([1, 2, 3])
    ...   return ctx.all_gather(local_value, axis=0)
    >>> result = strategy.run(gather_value)
    >>> result
    PerReplica:{
      0: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
      1: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>
    }
    >>> strategy.experimental_local_results(result)
    (<tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3],
    dtype=int32)>,
    <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3],
    dtype=int32)>)


    You can also pass in a nested structure of tensors to all-gather, say, a
    list:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> @tf.function
    ... def gather_nest():
    ...   ctx = tf.distribute.get_replica_context()
    ...   value_1 = tf.constant([1, 2, 3])
    ...   value_2 = tf.constant([[1, 2], [3, 4]])
    ...   # all_gather a nest of `tf.distribute.DistributedValues`
    ...   return ctx.all_gather([value_1, value_2], axis=0)
    >>> result = strategy.run(gather_nest)
    >>> result
    [PerReplica:{
      0: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
      1: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>
    }, PerReplica:{
      0: <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>,
      1: <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>
    }]
    >>> strategy.experimental_local_results(result)
    ([<tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
    <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>],
           [<tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
           <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>])


    What if you are all-gathering tensors with different shapes on different
    replicas? Consider the following example with two replicas, where you have
    `value` as a nested structure consisting of two items to all-gather, `a` and
    `b`.

    * On Replica 0, `value` is `{'a': [0], 'b': [[0, 1]]}`.
    * On Replica 1, `value` is `{'a': [1], 'b': [[2, 3], [4, 5]]}`.
    * Result for `all_gather` with `axis=0` (on each of the replicas) is:

      ```
      {'a': [1, 2], 'b': [[0, 1], [2, 3], [4, 5]]}
      ```

    Args:
      value: a nested structure of `tf.Tensor` which `tf.nest.flatten` accepts,
        or a `tf.distribute.DistributedValues` instance. The structure of the
        `tf.Tensor` need to be same on all replicas. The underlying tensor
        constructs can only be dense tensors with non-zero rank, NOT
        `tf.IndexedSlices`.
      axis: 0-D int32 Tensor. Dimension along which to gather.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
       A nested structure of `tf.Tensor` with the gathered values. The structure
       is the same as `value`.
    """
for v in nest.flatten(value):
    if isinstance(v, indexed_slices.IndexedSlices):
        raise NotImplementedError("all_gather does not support IndexedSlices")

if options is None:
    options = collective_util.Options()

def batch_all_gather(strategy, *value_flat):
    exit(strategy.extended._batch_gather_to(  # pylint: disable=protected-access
        [(v, _batch_reduce_destination(v)) for v in value_flat], axis,
        options))

@custom_gradient.custom_gradient
def grad_wrapper(*xs):
    ys = self.merge_call(batch_all_gather, args=xs)

    def grad(*dy_s):
        grads = self.all_reduce(reduce_util.ReduceOp.SUM, dy_s)
        new_grads = []
        for i, grad in enumerate(grads):
            input_shape = array_ops.shape(xs[i])
            axis_dim = array_ops.reshape(input_shape[axis], [1])
            with ops.control_dependencies([array_ops.identity(grads)]):
                d = self.all_gather(axis_dim, axis=0)
                begin_dim = math_ops.reduce_sum(d[:self.replica_id_in_sync_group])
                end_dim = begin_dim + array_ops.shape(xs[i])[axis]
                new_grad = array_ops.gather(
                    grad, axis=axis, indices=math_ops.range(begin_dim, end_dim))
                new_grads.append(new_grad)
        exit(new_grads)

    exit((ys, grad))

exit(nest.pack_sequence_as(value, grad_wrapper(*nest.flatten(value))))
