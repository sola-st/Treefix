# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adadelta.py
for v in var_list:
    self._zeros_slot(v, "accum", self._name)
    self._zeros_slot(v, "accum_update", self._name)
