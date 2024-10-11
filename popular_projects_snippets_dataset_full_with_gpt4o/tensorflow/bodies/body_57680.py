# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a SavedModel with deprecated TocoConverter."""
saved_model_dir = self._createSavedModel(shape=[1, 16, 16, 3])

# Convert model and ensure model is not None.
converter = lite.TocoConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Ensure the model is able to load.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
