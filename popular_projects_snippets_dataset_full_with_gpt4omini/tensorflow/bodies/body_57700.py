# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Sequential tf.keras model with deprecated TocoConverter."""
self._getSequentialModel()

converter = lite.TocoConverter.from_keras_model_file(self._keras_file)
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Ensure the model is able to load.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
