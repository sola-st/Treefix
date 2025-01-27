# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
input_data = constant_op.constant(1., shape=[1])
root = autotrackable.AutoTrackable()
root.f = def_function.function(lambda x: 2. * x)
to_save = root.f.get_concrete_function(input_data)

saved_model_dir = self._getFilepath('model')
save(root, saved_model_dir, to_save)

flags_str = '--saved_model_dir={}'.format(saved_model_dir)
self._run(flags_str, should_succeed=True)
