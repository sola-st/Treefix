# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model has debug info captured."""
with test_context():
    self._getSequentialModel()
    converter = lite.TFLiteConverter.from_keras_model_file(self._keras_file)
    converter.convert()
    self.assertValidDebugInfo(converter._debug_info)
