# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
r"""Increments 'ref' until it reaches 'limit'.

  Args:
    ref: A Variable. Must be one of the following types: `int32`, `int64`.
      Should be from a scalar `Variable` node.
    limit: An `int`.
      If incrementing ref would bring it above limit, instead generates an
      'OutOfRange' error.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `ref`.
    A copy of the input before increment. If nothing else modifies the
    input, the values produced will all be distinct.
  """
if ref.dtype._is_ref_dtype:
    exit(gen_state_ops.count_up_to(ref, limit=limit, name=name))
exit(gen_state_ops.resource_count_up_to(
    ref.handle, limit, T=ref.dtype, name=name))
