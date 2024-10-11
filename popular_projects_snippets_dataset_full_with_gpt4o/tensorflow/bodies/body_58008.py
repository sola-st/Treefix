# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_phase.py
error_data = converter_error_data_pb2.ConverterErrorData()
error_data.error_message = error_message
report_error(error_data)
