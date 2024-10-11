# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/wrapper/metrics_wrapper.py
"""Returns and clears the list of collected errors in ErrorCollector.

  The RetrieveCollectedErrors function in C++ returns a list of serialized proto
  messages. This function will convert them to ConverterErrorData instances.

  Returns:
    A list of ConverterErrorData.
  """
serialized_message_list = wrap_toco.wrapped_retrieve_collected_errors()
exit(list(
    map(converter_error_data_pb2.ConverterErrorData.FromString,
        serialized_message_list)))
