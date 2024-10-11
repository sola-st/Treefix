# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Invokes `fn` on each replica, with the given arguments.

    This method is the primary way to distribute your computation with a
    tf.distribute object. It invokes `fn` on each replica. If `args` or `kwargs`
    have `tf.distribute.DistributedValues`, such as those produced by a
    `tf.distribute.DistributedDataset` from
    `tf.distribute.Strategy.experimental_distribute_dataset` or
    `tf.distribute.Strategy.distribute_datasets_from_function`,
    when `fn` is executed on a particular replica, it will be executed with the
    component of `tf.distribute.DistributedValues` that correspond to that
    replica.

    `fn` is invoked under a replica context. `fn` may call
    `tf.distribute.get_replica_context()` to access members such as
    `all_reduce`. Please see the module-level docstring of tf.distribute for the
    concept of replica context.

    All arguments in `args` or `kwargs` can be a nested structure of tensors,
    e.g. a list of tensors, in which case `args` and `kwargs` will be passed to
    the `fn` invoked on each replica. Or `args` or `kwargs` can be
    `tf.distribute.DistributedValues` containing tensors or composite tensors,
    i.e. `tf.compat.v1.TensorInfo.CompositeTensor`, in which case each `fn` call
    will get the component of a `tf.distribute.DistributedValues` corresponding
    to its replica. Note that arbitrary Python values that are not of the types
    above are not supported.

    IMPORTANT: Depending on the implementation of `tf.distribute.Strategy` and
    whether eager execution is enabled, `fn` may be called one or more times. If
    `fn` is annotated with `tf.function` or `tf.distribute.Strategy.run` is
    called inside a `tf.function` (eager execution is disabled inside a
    `tf.function` by default), `fn` is called once per replica to generate a
    Tensorflow graph, which will then be reused for execution with new inputs.
    Otherwise, if eager execution is enabled, `fn` will be called once per
    replica every step just like regular python code.

    Example usage:

    1.  Constant tensor input.

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> tensor_input = tf.constant(3.0)
        >>> @tf.function
        ... def replica_fn(input):
        ...   return input*2.0
        >>> result = strategy.run(replica_fn, args=(tensor_input,))
        >>> result
        PerReplica:{
          0: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>,
          1: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>
        }

    2.  DistributedValues input.  {: value=2}

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> @tf.function
        ... def run():
        ...   def value_fn(value_context):
        ...     return value_context.num_replicas_in_sync
        ...   distributed_values = (
        ...     strategy.experimental_distribute_values_from_function(
        ...       value_fn))
        ...   def replica_fn2(input):
        ...     return input*2
        ...   return strategy.run(replica_fn2, args=(distributed_values,))
        >>> result = run()
        >>> result
        <tf.Tensor: shape=(), dtype=int32, numpy=4>

    3.  Use `tf.distribute.ReplicaContext` to allreduce values. {: value=3}

        >>> strategy = tf.distribute.MirroredStrategy(["gpu:0", "gpu:1"])
        >>> @tf.function
        ... def run():
        ...    def value_fn(value_context):
        ...      return tf.constant(value_context.replica_id_in_sync_group)
        ...    distributed_values = (
        ...        strategy.experimental_distribute_values_from_function(
        ...            value_fn))
        ...    def replica_fn(input):
        ...      return tf.distribute.get_replica_context().all_reduce(
        ...          "sum", input)
        ...    return strategy.run(replica_fn, args=(distributed_values,))
        >>> result = run()
        >>> result
        PerReplica:{
          0: <tf.Tensor: shape=(), dtype=int32, numpy=1>,
          1: <tf.Tensor: shape=(), dtype=int32, numpy=1>
        }

    Args:
      fn: The function to run on each replica.
      args: Optional positional arguments to `fn`. Its element can be a tensor,
        a nested structure of tensors or a `tf.distribute.DistributedValues`.
      kwargs: Optional keyword arguments to `fn`. Its element can be a tensor,
        a nested structure of tensors or a `tf.distribute.DistributedValues`.
      options: An optional instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Merged return value of `fn` across replicas. The structure of the return
      value is the same as the return value from `fn`. Each element in the
      structure can either be `tf.distribute.DistributedValues`, `Tensor`
      objects, or `Tensor`s (for example, if running on a single replica).
    """
del options

if not isinstance(args, (list, tuple)):
    raise ValueError(
        "positional args must be a list or tuple, got {}".format(type(args)))

with self.scope():
    # tf.distribute supports Eager functions, so AutoGraph should not be
    # applied when the caller is also in Eager mode.
    fn = autograph.tf_convert(
        fn, autograph_ctx.control_status_ctx(), convert_by_default=False)
    exit(self._extended.call_for_each_replica(fn, args=args, kwargs=kwargs))
