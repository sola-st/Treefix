# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Checks whether a tensor has been initialized.

  Outputs boolean scalar indicating whether the tensor has been initialized.

  Args:
    ref: A mutable `Tensor`.
      Should be from a `Variable` node. May be uninitialized.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """
if ref.dtype._is_ref_dtype:
    exit(gen_state_ops.is_variable_initialized(ref=ref, name=name))
# Handle resource variables.
exit(ref.is_initialized(name=name))
