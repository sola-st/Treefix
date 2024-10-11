# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
keras_file = self._getKerasModelFile()

flags_str = '--keras_model_file={}'.format(keras_file)
self._run(flags_str, should_succeed=True)
os.remove(keras_file)
