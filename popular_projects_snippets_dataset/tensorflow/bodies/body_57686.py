# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
if self._keras_file:
    os.remove(self._keras_file)
super(FromKerasFile, self).tearDown()
