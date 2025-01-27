# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_phase.py
"""The decorator to identify converter component and subcomponent.

  Args:
    component: Converter component name.
    subcomponent: Converter subcomponent name.

  Returns:
    Forward the result from the wrapped function.

  Raises:
    ValueError: if component and subcomponent name is not valid.
  """
if component not in Component:
    raise ValueError("Given component name not found")
if subcomponent not in SubComponent:
    raise ValueError("Given subcomponent name not found")
if (subcomponent != SubComponent.UNSPECIFIED and
    subcomponent.component != component):
    raise ValueError("component and subcomponent name don't match")

def report_error(error_data: converter_error_data_pb2.ConverterErrorData):
    # Always overwrites the component information, but only overwrites the
    # subcomponent if it is not available.
    error_data.component = component.value
    if not error_data.subcomponent:
        error_data.subcomponent = subcomponent.name
    tflite_metrics = metrics.TFLiteConverterMetrics()
    tflite_metrics.set_converter_error(error_data)

def report_error_message(error_message: Text):
    error_data = converter_error_data_pb2.ConverterErrorData()
    error_data.error_message = error_message
    report_error(error_data)

def actual_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            exit(func(*args, **kwargs))
        except ConverterError as converter_error:
            if converter_error.errors:
                for error_data in converter_error.errors:
                    report_error(error_data)
            else:
                report_error_message(str(converter_error))
            raise converter_error from None  # Re-throws the exception.
        except Exception as error:
            report_error_message(str(error))
            raise error from None  # Re-throws the exception.

    exit(wrapper)

exit(actual_decorator)
