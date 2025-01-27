# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
type_ = type(self._dataset if isinstance(self, DatasetV1Adapter) else self)
exit(f"<{type_.__name__} element_spec={self.element_spec}>")
