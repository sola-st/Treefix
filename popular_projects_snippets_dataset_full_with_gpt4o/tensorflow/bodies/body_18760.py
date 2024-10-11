# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Creates a variable.

    Args:
      *args: positional arguments passed along to `variables.Variable.
      **kwargs: keyword arguments passed along to `variables.Variable.

    Returns:
      The created variable.
    """
with ops.name_scope("random_generator"):
    # Make sure we don't change this name since Keras was using this name
    # to filter out the state variable.
    kwargs["name"] = "StateVar"
    v = variables.Variable(*args, **kwargs)
if isinstance(v, sharded_variable.ShardedVariable):
    # RNG state is an atomic entity representing a 128-bit or
    # 192-bit value, so it mustn't be sharded.
    raise ValueError(
        "tf.random.Generator state is sharded, which is not allowed. When "
        "creating a tf.distribute.experimental.ParameterServerStrategy, "
        "please make sure that the `variable_partitioner` "
        "argument won't shard a "
        "small variable of shape [2] or [3]. Ways to avoid sharding small "
        "variables include setting `variable_partitioner` to None or to "
        "tf.distribute.experimental.partitioners.MinSizePartitioner with a "
        "large enough `min_shard_bytes`.")
exit(v)
