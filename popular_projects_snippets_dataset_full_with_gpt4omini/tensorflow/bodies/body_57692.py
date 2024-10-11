# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model testing output arrays argument."""
ops.disable_eager_execution()
self._getSequentialModel()

# Invalid output array raises error.
with self.assertRaises(ValueError) as error:
    lite.TFLiteConverter.from_keras_model_file(
        self._keras_file, output_arrays=['invalid-output'])
self.assertEqual("Invalid tensors 'invalid-output' were found.",
                 str(error.exception))

# Valid output array.
converter = lite.TFLiteConverter.from_keras_model_file(
    self._keras_file, output_arrays=['time_distributed/Reshape_1'])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
