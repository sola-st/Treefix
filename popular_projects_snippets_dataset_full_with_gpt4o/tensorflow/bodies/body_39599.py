# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
self._primary_variable = primary_variable
self._mirrored_variable = mirrored_variable
tensor = self._primary_variable.read_value()
spec = saver_lib.BaseSaverBuilder.SaveSpec(
    tensor=tensor,
    slice_spec="",
    name=name)
super().__init__(tensor, [spec], name)
