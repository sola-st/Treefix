# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable.py
error_code_str = converter_error_data_pb2.ConverterErrorData.ErrorCode.Name(
    error_data.error_code)
_gauge_conversion_errors.get_cell(
    error_data.component,
    error_data.subcomponent,
    error_data.operator.name,
    error_code_str,
).set(error_data.error_message)
