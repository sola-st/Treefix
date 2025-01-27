# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
saved_model_dir, custom_opdefs_str = self._createSavedModelWithCustomOp()

# Valid conversion.
flags_str = (
    '--saved_model_dir={0} --custom_opdefs="{1}" --allow_custom_ops '
    '--experimental_new_converter'.format(saved_model_dir,
                                          custom_opdefs_str))
self._run(
    flags_str,
    should_succeed=True,
    expected_ops_in_converted_model=['CustomAdd'])
