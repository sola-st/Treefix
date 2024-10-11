# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_phase.py
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
