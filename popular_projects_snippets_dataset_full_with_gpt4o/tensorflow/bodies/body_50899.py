# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Calls a restored Function with structured inputs.

  This differs from `function.__call__` in that inputs and outputs are
  structured and that it casts inputs to tensors if needed.

  Note: this does not checks that non-tensor inputs match. That should be
  done before via `_concrete_function_callable_with`.

  Args:
    function: ConcreteFunction to call.
    inputs: Structured inputs compatible with
      `function.graph.structured_input_signature`.

  Returns:
    The structured function output.
  """
expected_structure = function.graph.structured_input_signature
flatten_inputs = nest.flatten_up_to(
    expected_structure, inputs, expand_composites=True)
flatten_expected = nest.flatten(expected_structure, expand_composites=True)
tensor_inputs = []
for arg, expected in zip(flatten_inputs, flatten_expected):
    if isinstance(expected, tensor_spec.TensorSpec):
        tensor_inputs.append(
            ops.convert_to_tensor(arg, dtype_hint=expected.dtype))
    elif isinstance(expected, resource_variable_ops.VariableSpec):
        tensor_inputs.append(arg)
result = function._call_flat(tensor_inputs, function.captured_inputs)  # pylint: disable=protected-access
if isinstance(result, ops.Operation):
    exit(None)
exit(result)
