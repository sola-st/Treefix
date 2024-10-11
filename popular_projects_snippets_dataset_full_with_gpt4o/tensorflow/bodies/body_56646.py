# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/python/modify_model_interface_lib.py
"""Modify a quantized model's interface (input/output) from float to integer.

  Args:
    input_file: Full path name to the input tflite file.
    output_file: Full path name to the output tflite file.
    input_type: Final input interface type.
    output_type: Final output interface type.

  Raises:
    RuntimeError: If the modification of the model interface was unsuccessful.
    ValueError: If the input_type or output_type is unsupported.

  """
# Map the interface types to integer values
input_type_int = _parse_type_to_int(input_type, 'input_type')
output_type_int = _parse_type_to_int(output_type, 'output_type')

# Invoke the function to modify the model interface
status = _pywrap_modify_model_interface.modify_model_interface(
    input_file, output_file, input_type_int, output_type_int)

# Throw an exception if the return status is an error.
if status != 0:
    raise RuntimeError(
        'Error occurred when trying to modify the model input type from float '
        'to {input_type} and output type from float to {output_type}.'.format(
            input_type=input_type, output_type=output_type))
