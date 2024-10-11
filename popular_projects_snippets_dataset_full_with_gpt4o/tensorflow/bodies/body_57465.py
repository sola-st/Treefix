# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
keras_file = self._getKerasModelFile()
log_dir = self.get_temp_dir()

flags_str = ('--keras_model_file={} --experimental_new_converter=false '
             '--conversion_summary_dir={}'.format(keras_file, log_dir))
self._run(flags_str, should_succeed=True)
os.remove(keras_file)

num_items_conversion_summary = len(os.listdir(log_dir))
self.assertEqual(num_items_conversion_summary, 0)
