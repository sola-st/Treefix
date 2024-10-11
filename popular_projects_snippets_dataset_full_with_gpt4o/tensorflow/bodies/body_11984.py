# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Create a variable Operation.

  See also variables.Variable.

  Args:
    shape: The shape of the tensor managed by this variable
    dtype: The underlying type of the tensor values.
    name: optional name to use for the variable op.
    container: An optional string. Defaults to "".
      If non-empty, this variable is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional string. Defaults to "".
      If non-empty, this variable is named in the given bucket
      with this shared_name. Otherwise, the node name is used instead.

  Returns:
    A variable tensor.
  """
exit(gen_state_ops.variable_v2(
    shape=shape,
    dtype=dtype,
    name=name,
    container=container,
    shared_name=shared_name))
