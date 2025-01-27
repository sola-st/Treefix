# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# pylint: disable=protected-access
exit((isinstance(other, TensorArraySpec) and
        self._dtype == other._dtype and
        self._dynamic_size == other._dynamic_size))
