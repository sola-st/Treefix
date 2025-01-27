# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
# pylint: disable=protected-access
exit((type(self) is type(other) and self._shape == other._shape and
        self._dtype == other._dtype and self._name == other._name))
