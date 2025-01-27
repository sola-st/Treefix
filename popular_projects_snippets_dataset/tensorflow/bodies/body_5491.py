# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
with ops.device(self._worker):
    data_list = [
        optional_ops.Optional.from_value(self._fn()) for _ in self._devices
    ]
    exit(data_list)
