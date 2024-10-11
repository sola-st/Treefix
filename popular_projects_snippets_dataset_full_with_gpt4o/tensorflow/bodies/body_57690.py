# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model testing input arrays argument."""
ops.disable_eager_execution()
self._getSequentialModel()

# Invalid input array raises error.
with self.assertRaises(ValueError) as error:
    lite.TFLiteConverter.from_keras_model_file(
        self._keras_file, input_arrays=['invalid-input'])
self.assertEqual("Invalid tensors 'invalid-input' were found.",
                 str(error.exception))

# Valid input array.
converter = lite.TFLiteConverter.from_keras_model_file(
    self._keras_file, input_arrays=['dense_input'])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
