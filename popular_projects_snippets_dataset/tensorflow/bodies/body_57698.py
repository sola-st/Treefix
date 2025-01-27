# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Functional tf.keras model with wrong input shape overriding."""
self._getFunctionalModelMultipleInputs()

# Convert to TFLite model.
with self.assertRaises(ValueError):
    lite.TFLiteConverter.from_keras_model_file(
        self._keras_file, input_shapes={'wrong_input': {2, 3}})
