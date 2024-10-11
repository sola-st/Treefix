# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Reduce `value` across replicas and return result on current device.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> def step_fn():
    ...   i = tf.distribute.get_replica_context().replica_id_in_sync_group
    ...   return tf.identity(i)
    >>>
    >>> per_replica_result = strategy.run(step_fn)
    >>> total = strategy.reduce("SUM", per_replica_result, axis=None)
    >>> total
    <tf.Tensor: shape=(), dtype=int32, numpy=1>

    To see how this would look with multiple replicas, consider the same
    example with MirroredStrategy with 2 GPUs:

    ```python
    strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
    def step_fn():
      i = tf.distribute.get_replica_context().replica_id_in_sync_group
      return tf.identity(i)

    per_replica_result = strategy.run(step_fn)
    # Check devices on which per replica result is:
    strategy.experimental_local_results(per_replica_result)[0].device
    # /job:localhost/replica:0/task:0/device:GPU:0
    strategy.experimental_local_results(per_replica_result)[1].device
    # /job:localhost/replica:0/task:0/device:GPU:1

    total = strategy.reduce("SUM", per_replica_result, axis=None)
    # Check device on which reduced result is:
    total.device
    # /job:localhost/replica:0/task:0/device:CPU:0

    ```

    This API is typically used for aggregating the results returned from
    different replicas, for reporting etc. For example, loss computed from
    different replicas can be averaged using this API before printing.

    Note: The result is copied to the "current" device - which would typically
    be the CPU of the worker on which the program is running. For `TPUStrategy`,
    it is the first TPU host. For multi client `MultiWorkerMirroredStrategy`,
    this is CPU of each worker.

    There are a number of different tf.distribute APIs for reducing values
    across replicas:
    * `tf.distribute.ReplicaContext.all_reduce`: This differs from
    `Strategy.reduce` in that it is for replica context and does
    not copy the results to the host device. `all_reduce` should be typically
    used for reductions inside the training step such as gradients.
    * `tf.distribute.StrategyExtended.reduce_to` and
    `tf.distribute.StrategyExtended.batch_reduce_to`: These APIs are more
    advanced versions of `Strategy.reduce` as they allow customizing the
    destination of the result. They are also called in cross replica context.

    _What should axis be?_

    Given a per-replica value returned by `run`, say a
    per-example loss, the batch will be divided across all the replicas.  This
    function allows you to aggregate across replicas and optionally also across
    batch elements by specifying the axis parameter accordingly.

    For example, if you have a global batch size of 8 and 2
    replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and
    `[4, 5, 6, 7]` will be on replica 1. With `axis=None`, `reduce` will
    aggregate only across replicas, returning `[0+4, 1+5, 2+6, 3+7]`.
    This is useful when each replica is computing a scalar or some other value
    that doesn't have a "batch" dimension (like a gradient or loss).
    ```
    strategy.reduce("sum", per_replica_result, axis=None)
    ```

    Sometimes, you will want to aggregate across both the global batch _and_
    all replicas. You can get this behavior by specifying the batch
    dimension as the `axis`, typically `axis=0`. In this case it would return a
    scalar `0+1+2+3+4+5+6+7`.
    ```
    strategy.reduce("sum", per_replica_result, axis=0)
    ```

    If there is a last partial batch, you will need to specify an axis so
    that the resulting shape is consistent across replicas. So if the last
    batch has size 6 and it is divided into [0, 1, 2, 3] and [4, 5], you
    would get a shape mismatch unless you specify `axis=0`. If you specify
    `tf.distribute.ReduceOp.MEAN`, using `axis=0` will use the correct
    denominator of 6. Contrast this with computing `reduce_mean` to get a
    scalar value on each replica and this function to average those means,
    which will weigh some values `1/8` and others `1/4`.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value: a `tf.distribute.DistributedValues` instance, e.g. returned by
        `Strategy.run`, to be combined into a single tensor. It can also be a
        regular tensor when used with `OneDeviceStrategy` or default strategy.
      axis: specifies the dimension to reduce along within each
        replica's tensor. Should typically be set to the batch dimension, or
        `None` to only reduce across replicas (e.g. if the tensor has no batch
        dimension).

    Returns:
      A `Tensor`.
    """
# TODO(josh11b): support `value` being a nest.
_require_cross_replica_or_default_context_extended(self._extended)
if isinstance(reduce_op, six.string_types):
    reduce_op = reduce_util.ReduceOp(reduce_op.upper())
if axis is None:
    exit(self._extended._reduce(reduce_op, value))  # pylint: disable=protected-access
if reduce_op == reduce_util.ReduceOp.SUM:

    def reduce_sum(v):
        exit(math_ops.reduce_sum(v, axis=axis))

    if eager_context.executing_eagerly():
        # As some strategies (e.g. TPUStrategy) doesn't support pure eager
        # execution, wrap the `reduce_sum_fn` with a `tf.function` so it can be
        # run from eager mode. Cache the tf.function by `axis` to avoid the
        # same function to be traced again.
        if axis not in self._reduce_sum_fns:

            def reduce_sum_fn(v):
                exit(self.run(reduce_sum, args=(v,)))

            self._reduce_sum_fns[axis] = def_function.function(reduce_sum_fn)
        value = self._reduce_sum_fns[axis](value)
    else:
        value = self.run(reduce_sum, args=(value,))

    exit(self._extended._reduce(reduce_op, value))  # pylint: disable=protected-access
if reduce_op != reduce_util.ReduceOp.MEAN:
    raise TypeError("Expected `reduce_op` to be a `tf.distribute.ReduceOp`, "
                    "not: %r" % reduce_op)

def mean_reduce_helper(v, axes=axis):
    """Computes the numerator and denominator on each replica."""
    numer = math_ops.reduce_sum(v, axis=axes)
    def dimension(axis):
        if v.shape.rank is not None:
            # Note(joshl): We support axis < 0 to be consistent with the
            # tf.math.reduce_* operations.
            if axis < 0:
                if axis + v.shape.rank < 0:
                    raise ValueError(
                        "`axis` = %r out of range for `value` with rank %d" %
                        (axis, v.shape.rank))
                axis += v.shape.rank
            elif axis >= v.shape.rank:
                raise ValueError(
                    "`axis` = %r out of range for `value` with rank %d" %
                    (axis, v.shape.rank))
            # TF v2 returns `None` for unknown dimensions and an integer for
            # known dimension, whereas TF v1 returns tensor_shape.Dimension(None)
            # or tensor_shape.Dimension(integer). `dimension_value` hides this
            # difference, always returning `None` or an integer.
            dim = tensor_shape.dimension_value(v.shape[axis])
            if dim is not None:
                # By returning a python value in the static shape case, we can
                # maybe get a fast path for reducing the denominator.
                # TODO(b/151871486): Remove array_ops.identity after we fallback to
                # simple reduction if inputs are all on CPU.
                exit(array_ops.identity(
                    constant_op.constant(dim, dtype=dtypes.int64)))
        elif axis < 0:
            axis = axis + array_ops.rank(v)
        # TODO(b/151871486): Remove array_ops.identity after we fallback to
        # simple reduction if inputs are all on CPU.
        exit(array_ops.identity(
            array_ops.shape_v2(v, out_type=dtypes.int64)[axis]))
    if isinstance(axis, six.integer_types):
        denom = dimension(axis)
    elif isinstance(axis, (tuple, list)):
        denom = math_ops.reduce_prod([dimension(a) for a in axes])
    else:
        raise TypeError(
            "Expected `axis` to be an integer, tuple or list not: %r" % axis)
    # TODO(josh11b): Should we cast denom to v.dtype here instead of after the
    # reduce is complete?
    exit((numer, denom))

if eager_context.executing_eagerly():
    # As some strategies (e.g. TPUStrategy) doesn't support pure eager
    # execution, wrap the `mean_reduce_helper` with a `tf.function` so it can
    # be run from eager mode. Cache the tf.function by `axis` to avoid the
    # same function to be traced again.
    if axis not in self._mean_reduce_helper_fns:

        def mean_reduce_fn(v):
            exit(self.run(mean_reduce_helper, args=(v,)))

        self._mean_reduce_helper_fns[axis] = def_function.function(
            mean_reduce_fn)
    numer, denom = self._mean_reduce_helper_fns[axis](value)
else:
    numer, denom = self.run(mean_reduce_helper, args=(value,))

# TODO(josh11b): Should batch reduce here instead of doing two.
numer = self._extended._reduce(reduce_util.ReduceOp.SUM, numer)  # pylint: disable=protected-access
denom = self._extended._reduce(reduce_util.ReduceOp.SUM, denom)  # pylint: disable=protected-access
denom = math_ops.cast(denom, numer.dtype)
exit(math_ops.truediv(numer, denom))
