# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
exit((isinstance(other, DatasetSpec) and
        self._element_spec == other._element_spec and
        self._dataset_shape == other._dataset_shape))
