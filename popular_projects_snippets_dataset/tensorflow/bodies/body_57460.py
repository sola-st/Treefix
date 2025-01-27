# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
saved_model_dir, custom_opdefs_str = self._createSavedModelWithCustomOp(
    opname='CustomAdd2')

# Valid conversion. OpDef already registered.
flags_str = ('--saved_model_dir={0} --allow_custom_ops '
             '--custom_opdefs="{1}" '
             '--experimental_new_converter '
             '--experimental_select_user_tf_ops=CustomAdd2 '
             '--target_ops=TFLITE_BUILTINS,SELECT_TF_OPS'.format(
                 saved_model_dir, custom_opdefs_str))
self._run(
    flags_str,
    should_succeed=True,
    expected_ops_in_converted_model=['FlexCustomAdd2'])
