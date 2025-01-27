# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
self._primary_variable = primary_variable
self._mirrored_variable = mirrored_variable
super(_MirroringSaveable, self).__init__(
    self._primary_variable, "", name)
