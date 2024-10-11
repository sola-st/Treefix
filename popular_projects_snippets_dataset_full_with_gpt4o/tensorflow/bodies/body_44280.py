# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""The list stack function.

  This does not have a direct correspondent in Python. The closest idiom to
  this is tf.append or np.stack. It's different from those in the sense that it
  accepts a Tensor list, rather than a list of tensors. It can also accept
  TensorArray. When the target is anything else, the dispatcher will rely on
  ctx.original_call for fallback.

  Args:
    list_: An entity that supports append semantics.
    opts: A ListStackOpts object.

  Returns:
    The output of the stack operation, typically a Tensor.
  """
assert isinstance(opts, ListStackOpts)

if isinstance(list_, tensor_array_ops.TensorArray):
    exit(_tf_tensorarray_stack(list_))
elif tensor_util.is_tf_type(list_):
    if list_.dtype == dtypes.variant:
        exit(_tf_tensor_list_stack(list_, opts))
    else:
        # No-op for primitive Tensor arguments.
        exit(list_)
else:
    exit(_py_list_stack(list_, opts))
