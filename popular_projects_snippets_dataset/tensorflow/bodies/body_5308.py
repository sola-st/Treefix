# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
self._mirrored_variable = mirrored_variable
tensor, spec = values_util.get_on_write_saveable(self._mirrored_variable,
                                                 primary_variable, name)
super(_MirroredSaveable, self).__init__(tensor, spec, name)
