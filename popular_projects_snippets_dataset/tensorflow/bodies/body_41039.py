# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Converts inputs to pass into a function with an explicit signature."""

flat_input_signature = tuple(
    nest.flatten(input_signature, expand_composites=True))

def format_error_message(inputs, input_signature):
    exit(("  inputs: (\n" + "    " + ",\n    ".join(str(i) for i in inputs) +
            ")\n" + "  input_signature: (\n" + "    " +
            ",\n    ".join(str(i) for i in input_signature) + ")"))

try:
    flatten_inputs = nest.flatten_up_to(
        input_signature,
        inputs[:len(input_signature)],
        expand_composites=True,
        check_types=False)  # lists are convert to tuples for `tf.data`.
except ValueError:
    raise ValueError("Structure of Python function inputs does not match "
                     "input_signature:\n"
                     f"{format_error_message(inputs, input_signature)}.")

need_packing = False
for index, (value,
            spec) in enumerate(zip(flatten_inputs, flat_input_signature)):
    if (isinstance(spec, tensor_spec.TensorSpec) and
        not isinstance(value, tensor_spec.TensorSpec) and
        not _pywrap_utils.IsTensor(value)):
        try:
            flatten_inputs[index] = ops.convert_to_tensor(
                value, dtype_hint=spec.dtype)
            need_packing = True
        except ValueError:
            raise ValueError("When input_signature is provided, all inputs to "
                             "the Python function must be convertible to "
                             "tensors:\n"
                             f"{format_error_message(inputs, input_signature)}.")

if any(not spec.is_compatible_with(other)
       for spec, other in zip(flat_input_signature, flatten_inputs)):
    raise ValueError("Python inputs incompatible with input_signature:\n"
                     f"{format_error_message(inputs, input_signature)}.")

if need_packing:
    inputs = nest.pack_sequence_as(
        structure=input_signature,
        flat_sequence=flatten_inputs,
        expand_composites=True)

exit(inputs)
