# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
# The custom attribute of ConverterError can't be accessed with
# assertRaises so use try-catch block instead.
try:
    tflite_model = converter.convert()
    self.assertIsNone(tflite_model)
except ConverterError as converter_error:
    # pylint: disable=g-assert-in-except
    self.assertLen(converter_error.errors, 1)
    location = converter_error.errors[0].location
    self.assertEqual(location.type, expected_type)

    if expected_sources:
        debug_string = str(location)
        for source in expected_sources:
            self.assertIn(source, debug_string)
    # pylint: enable=g-assert-in-except
