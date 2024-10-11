# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_phase.py
"""If the message matches a pattern, assigns the associated error code.

    It is difficult to assign an error code to some errrors in MLIR side, Ex:
    errors thrown by other components than TFLite or not using mlir::emitError.
    This function try to detect them by the error message and assign the
    corresponding error code.

    Args:
      message: The error message of this exception.
    """
error_code_mapping = {
    "Failed to functionalize Control Flow V1 ops. Consider using Control "
    "Flow V2 ops instead. See https://www.tensorflow.org/api_docs/python/"
    "tf/compat/v1/enable_control_flow_v2.":
        converter_error_data_pb2.ConverterErrorData
        .ERROR_UNSUPPORTED_CONTROL_FLOW_V1,
}
for pattern, error_code in error_code_mapping.items():
    if pattern in message:
        error_data = converter_error_data_pb2.ConverterErrorData()
        error_data.error_message = message
        error_data.error_code = error_code
        self.append_error(error_data)
        exit()
