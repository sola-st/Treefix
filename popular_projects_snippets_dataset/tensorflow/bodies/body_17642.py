# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/partitioned_variables.py
"""Create a list of partitioned variables according to the given `slicing`.

  Currently only one dimension of the full variable can be sliced, and the
  full variable can be reconstructed by the concatenation of the returned
  list along that dimension.

  Args:
    shape: List of integers.  The shape of the full variable.
    slicing: List of integers.  How to partition the variable.
      Must be of the same length as `shape`.  Each value
      indicate how many slices to create in the corresponding
      dimension.  Presently only one of the values can be more than 1;
      that is, the variable can only be sliced along one dimension.

      For convenience, The requested number of partitions does not have to
      divide the corresponding dimension evenly.  If it does not, the
      shapes of the partitions are incremented by 1 starting from partition
      0 until all slack is absorbed.  The adjustment rules may change in the
      future, but as you can save/restore these variables with different
      slicing specifications this should not be a problem.
    initializer: A `Tensor` of shape `shape` or a variable initializer
      function.  If a function, it will be called once for each slice,
      passing the shape and data type of the slice as parameters.  The
      function must return a tensor with the same shape as the slice.
    dtype: Type of the variables. Ignored if `initializer` is a `Tensor`.
    trainable: If True also add all the variables to the graph collection
      `GraphKeys.TRAINABLE_VARIABLES`.
    collections: List of graph collections keys to add the variables to.
      Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
    name: Optional name for the full variable.  Defaults to
      `"PartitionedVariable"` and gets uniquified automatically.
    reuse: Boolean or `None`; if `True` and name is set, it would reuse
      previously created variables. if `False` it will create new variables.
      if `None`, it would inherit the parent scope reuse.

  Returns:
    A list of Variables corresponding to the slicing.

  Raises:
    ValueError: If any of the arguments is malformed.
  """
if len(shape) != len(slicing):
    raise ValueError(
        "The 'shape' and 'slicing' of a partitioned Variable "
        f"must have the length: shape: {shape}, slicing: {slicing}")
if len(shape) < 1:
    raise ValueError("A partitioned Variable must have rank at least 1: "
                     f"shape: {shape}")

# Legacy: we are provided the slicing directly, so just pass it to
# the partitioner.
partitioner = lambda **unused_kwargs: slicing

with variable_scope.variable_scope(
    name, "PartitionedVariable", reuse=reuse):
    # pylint: disable=protected-access
    partitioned_var = variable_scope._get_partitioned_variable(
        name=None,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        trainable=trainable,
        partitioner=partitioner,
        collections=collections)
    exit(list(partitioned_var))
    # pylint: enable=protected-access
