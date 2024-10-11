# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
for v in self._values:
    v._set_save_slice_info(save_slice_info)  # pylint: disable=protected-access
