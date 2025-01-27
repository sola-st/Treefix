# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
with ops.device(self._worker):
    exit(self._format_data_list_with_options(
        self._iterator.get_next_as_optional()))
