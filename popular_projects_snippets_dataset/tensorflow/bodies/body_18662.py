# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Helper to check the validity of arguments to a create_file_writer() call.

  Args:
    inside_function: whether the create_file_writer() call is in a tf.function
    **kwargs: the arguments to check, as kwargs to give them names.

  Raises:
    ValueError: if the arguments are graph tensors.
  """
for arg_name, arg in kwargs.items():
    if not isinstance(arg, ops.EagerTensor) and tensor_util.is_tf_type(arg):
        if inside_function:
            raise ValueError(
                f"Invalid graph Tensor argument '{arg_name}={arg}' to "
                "create_file_writer() inside an @tf.function. The create call will "
                "be lifted into the outer eager execution context, so it cannot "
                "consume graph tensors defined inside the function body.")
        else:
            raise ValueError(
                f"Invalid graph Tensor argument '{arg_name}={arg}' to eagerly "
                "executed create_file_writer().")
