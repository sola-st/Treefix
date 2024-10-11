# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
saved_model_dir, _ = self._createSavedModelWithCustomOp()

invalid_custom_opdefs_str = (
    'name: \'CustomAdd\' input_arg: {name: \'Input1\' type: DT_FLOAT} '
    'output_arg: {name: \'Output\' type: DT_FLOAT}')

# Valid conversion.
flags_str = (
    '--saved_model_dir={0} --custom_opdefs="{1}" --allow_custom_ops '
    '--experimental_new_converter'.format(saved_model_dir,
                                          invalid_custom_opdefs_str))
self._run(flags_str, should_succeed=False)
