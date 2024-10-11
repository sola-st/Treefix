# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
saved_model_dir, _ = self._createSavedModelWithCustomOp()

# Ensure --custom_opdefs.
flags_str = ('--saved_model_dir={0} --allow_custom_ops '
             '--experimental_new_converter'.format(saved_model_dir))
self._run(flags_str, should_succeed=False)
