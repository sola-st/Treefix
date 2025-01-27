# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
keras_file = self._getKerasFunctionalModelFile()

flags_str = '--keras_model_file={}'.format(keras_file)
self._run(flags_str, should_succeed=True,
          expected_output_shapes=[[1, 1], [1, 2]])
os.remove(keras_file)
