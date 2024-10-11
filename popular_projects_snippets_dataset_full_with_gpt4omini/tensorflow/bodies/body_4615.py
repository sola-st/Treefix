# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
if values_util.is_saving_non_distributed():
    exit(self._variables[0].initializer)
exit(super().initializer)
