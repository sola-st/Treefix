# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
self._run(
    '--keras_model_file=model.h5 --saved_model_dir=/tmp/',
    should_succeed=False)
