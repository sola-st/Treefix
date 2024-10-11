# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
"""Emits an HLO `CustomCall` operation with multiple outputs.

  See `CustomCall` specification at
    https://tensorflow.org/xla/operation_semantics#customcall,
  and `mhlo.custom_call` specification at
    https://tensorflow.org/mlir/hlo_ops#mhlocustom_call_mlirmhlocustomcallop.

  Args:
    call_target_name: Name of the user function. The function signature must
      conform to version 3 of the API, see
      `API_VERSION_STATUS_RETURNING_UNIFIED`. All operands and results assumed
      to be in the default layout.
    operands: A sequence of tensors with possibly different types.
    result_specs: A sequence of tensor specs for all results.
    backend_config: A string that encodes a metadata for the backend. Empty
      string by default.
    has_side_effect: Indicates whether the custom call has side effects. `False`
      by default.
    name: Optional name of the operation.

  Returns:
    A tuple of output tensors.
  """
exit(gen_xla_ops.xla_custom_call_v2(
    operands=operands,
    call_target_name=call_target_name,
    backend_config="" if backend_config is None else backend_config,
    has_side_effect=False if has_side_effect is None else has_side_effect,
    result_dtypes=tuple(spec.dtype for spec in result_specs),
    result_shapes=tuple(spec.shape for spec in result_specs),
    name=name,
))
