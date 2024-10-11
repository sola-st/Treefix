# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
"""Asserts that converted parameters have the expected values & types."""
self.assertLen(actual_params, len(expected_params))
for actual, expected in zip(actual_params, expected_params):
    if isinstance(expected, list):
        self.assertIsInstance(actual, list)
        self.assertLen(actual, len(expected))
        for actual_item, expected_item in zip(actual, expected):
            self.assertParamEqual(actual_item, expected_item)
    else:
        self.assertParamEqual(actual, expected)
